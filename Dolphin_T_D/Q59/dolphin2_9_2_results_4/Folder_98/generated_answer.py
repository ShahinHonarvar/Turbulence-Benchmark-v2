def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    left_truncatable_primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)