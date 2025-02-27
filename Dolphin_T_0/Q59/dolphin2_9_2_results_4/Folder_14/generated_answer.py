def all_left_truncatable_prime(int_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if num < 10:
            return False
        n = num
        while n:
            if n % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True

    def recursive_search(x):
        if x == 0:
            return
        else:
            if is_left_truncatable_prime(x):
                primes.append(x)
            recursive_search(x - 1)
    primes = []
    x = int_tuple[78]
    recursive_search(x)
    return sorted(primes, reverse=True)