def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[100]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)