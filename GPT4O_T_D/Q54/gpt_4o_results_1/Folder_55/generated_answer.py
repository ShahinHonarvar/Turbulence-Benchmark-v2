def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncatable_primes(limit):
        primes = []

        def helper(num):
            if is_prime(num):
                primes.append(num)
                for digit in range(10):
                    if num * 10 + digit < limit:
                        helper(num * 10 + digit)
        for i in range(1, 10):
            helper(i)
        return primes
    if len(numbers) <= 73:
        return []
    x = numbers[73]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)