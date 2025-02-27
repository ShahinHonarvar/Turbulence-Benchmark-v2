def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[992]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if is_prime(trunc):
                    trunc //= 10
                else:
                    break
                if trunc == 0:
                    primes.append(num)
    return sorted(primes)