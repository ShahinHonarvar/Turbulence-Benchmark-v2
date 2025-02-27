def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[86]
    primes = []
    for i in reversed(range(2, x)):
        if is_prime(i):
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)