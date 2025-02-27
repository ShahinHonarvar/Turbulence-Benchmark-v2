def prime_factors(li):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    num = li[0]
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set