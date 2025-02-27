from itertools import count, islice

def all_right_truncatable_prime(arg):

    def is_prime(n):
        div = 2
        while div * div <= n:
            if n % div == 0:
                return False
            div += 1
        return True
    [x] = arg
    return sorted([n for n in islice(count(2), x + 1) if is_prime(n) and all((is_prime(int(str(n)[:-i])) for i in range(1, len(str(n)))))])