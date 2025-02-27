import math

def all_left_truncatable_prime(x):

    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatables = [2, 3, 5, 7]
    n = 1
    while left_truncatables[-1] < x:
        digits = [int(t) for t in str(n)]
        if all((is_prime(int(''.join(digits[i:]))) for i in range(len(digits)))):
            left_truncatables.append(n)
        n += 2
    return sorted(left_truncatables)