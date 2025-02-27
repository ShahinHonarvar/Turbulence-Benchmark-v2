def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[81]
    primes = []
    for i in range(x):
        if is_prime(i):
            j = i
            while j != 0:
                if is_prime(j):
                    j //= 10
                else:
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)