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
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                prime_factors_list.append(i)
                n //= i
        return prime_factors_list
    if len(lst) <= 459:
        return set()
    return set(find_prime_factors(lst[459]))