def prime_factors(lst):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    num = lst[21]
    prime_set = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set