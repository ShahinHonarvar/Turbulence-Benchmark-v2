from math import sqrt

def all_left_right_truncatable_prime(x):
    c = []
    p = [i for i in range(2, x + 1) if i not in c]

    def is_prime(n):
        return all((n % d for d in range(2, int(sqrt(n)) + 1)))

    def is_truncatable(num):
        s = str(num)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:-i])) for i in range(1, len(s))))
    return sorted([num for num in p if num in range(100, x + 1) and is_truncatable(num)], reverse=True)