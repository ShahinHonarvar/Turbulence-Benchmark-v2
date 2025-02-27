from math import sqrt

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n <= 1 or n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[:i])):
                return False
        return is_prime(int(str_n))
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)