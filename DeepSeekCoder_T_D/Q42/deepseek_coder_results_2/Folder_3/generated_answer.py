def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_prime_factors(n):
        prime_factors_list = []
        while n % 2 == 0:
            prime_factors_list.append(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                prime_factors_list.append(i)
                n //= i
        if n > 2:
            prime_factors_list.append(n)
        return set(prime_factors_list)
    if len(lst) <= 100:
        return set()
    return find_prime_factors(lst[100])