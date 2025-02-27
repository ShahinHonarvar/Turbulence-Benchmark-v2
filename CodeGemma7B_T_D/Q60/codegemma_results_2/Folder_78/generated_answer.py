def all_left_right_truncatable_prime(x):

    def is_prime(y):
        if y in [0, 1]:
            return False
        elif y <= 3:
            return True
        elif y % 2 == 0 or y % 3 == 0:
            return False
        i = 5
        while i * i <= y:
            if y % i == 0 or y % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:i])):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result