from math import sqrt
    from itertools import count

def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def generate_primes():
        for n in count(2):
            if is_prime(n):
                yield n
    primes = generate_primes()
    prime_list = [p for p in primes if p < x]
    result = []
    for p in prime_list:
        temp = p
        while temp > 0:
            temp //= 10
            if temp in prime_list:
                result.append(p)
                break
    return sorted(result)