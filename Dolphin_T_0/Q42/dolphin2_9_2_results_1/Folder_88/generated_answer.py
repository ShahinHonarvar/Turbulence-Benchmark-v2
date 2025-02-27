def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    lst_46 = lst[46]
    prime_set = set()
    for i in range(2, lst_46 + 1):
        while lst_46 % i == 0:
            if is_prime(i):
                prime_set.add(i)
            lst_46 //= i
    return prime_set