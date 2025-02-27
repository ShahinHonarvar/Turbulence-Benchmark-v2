def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = []
    for n in range(11, x + 1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_truncatable_prime = True
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)