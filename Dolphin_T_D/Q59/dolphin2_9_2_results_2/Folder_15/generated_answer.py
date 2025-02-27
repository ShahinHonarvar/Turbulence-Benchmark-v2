def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[6]
    left_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        if '0' in str(n):
            continue
        truncation = n
        while truncation:
            if not is_prime(truncation):
                break
            truncation //= 10
        else:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)