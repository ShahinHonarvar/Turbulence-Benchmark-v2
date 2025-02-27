def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[24]
    primes = []
    for num in range(2, x):
        d = len(str(num))
        if is_prime(num):
            trunc = num
            while d > 1:
                trunc //= 10
                d -= 1
                if not is_prime(trunc):
                    break
            else:
                primes.append(num)
    return sorted(primes)