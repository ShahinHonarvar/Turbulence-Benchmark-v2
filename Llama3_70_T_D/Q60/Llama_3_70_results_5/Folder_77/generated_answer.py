def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    truncatable_primes = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_prime(n):
            str_n = str(n)
            is_truncatable = True
            for i in range(1, len(str_n)):
                left = int(str_n[i:])
                right = int(str_n[:-i])
                if not is_prime(left) or not is_prime(right):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)