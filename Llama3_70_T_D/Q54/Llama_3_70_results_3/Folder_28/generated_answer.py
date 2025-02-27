def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[19]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            j = i
            while j > 0:
                j //= 10
                if j > 0 and (not is_prime(j)):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)