def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[767]
    truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        is_truncatable = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[:len(str_i) - j])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)