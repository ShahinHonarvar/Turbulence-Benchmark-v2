def all_right_truncatable_prime(t):

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

    def is_right_truncatable_prime(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    result = []
    if len(t) <= 30:
        return result
    x = t[30]
    candidates = [2, 3, 5, 7]
    while candidates:
        num = candidates.pop()
        if num < x:
            result.append(num)
            for digit in range(10):
                new_num = num * 10 + digit
                if is_prime(new_num):
                    candidates.append(new_num)
    return sorted(result)