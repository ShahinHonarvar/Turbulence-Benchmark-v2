def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return [i for i in range(2, n + 1) if n % i == 0]
    if len(lst) <= 18:
        return set()
    num = lst[18]
    return {f for f in factors(num) if is_prime(f)}