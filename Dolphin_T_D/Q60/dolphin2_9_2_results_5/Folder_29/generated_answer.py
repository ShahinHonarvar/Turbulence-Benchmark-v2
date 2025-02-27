def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = num_tuple[55]
    res = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if is_prime(i):
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                if temp < 10:
                    res.append(temp)
                    break
                temp = temp // 10
                temp = temp * 10 + temp % 10
            if temp in res:
                res.remove(temp)
    return res