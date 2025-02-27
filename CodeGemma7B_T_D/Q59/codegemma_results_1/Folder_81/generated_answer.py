from itertools import count, islice

def all_left_truncatable_prime(t):

    def is_prime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in islice(count(5), int(n ** 0.5) - 2):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    return sorted([n for n in range(2, t[98]) if is_prime(n) and all((is_prime(int(str(n)[k:])) for k in range(len(str(n)))))])