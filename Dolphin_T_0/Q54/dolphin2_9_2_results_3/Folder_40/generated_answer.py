def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sq = int(n ** 0.5) + 1
        for divisor in range(3, sq, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    primes = []
    if x < 10:
        return primes
    for num in range(11, x):
        if is_prime(num) and is_right_truncatable(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes