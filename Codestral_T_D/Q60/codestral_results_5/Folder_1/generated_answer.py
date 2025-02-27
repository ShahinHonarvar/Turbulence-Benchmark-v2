def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    x = t[20]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            num = i
            while num > 0:
                num = truncate_left(num)
                if not is_prime(num):
                    break
            if num > 0:
                continue
            num = i
            while num > 0:
                num = truncate_right(num)
                if not is_prime(num):
                    break
            if num > 0:
                continue
            result.append(i)
    return sorted(result, reverse=True)