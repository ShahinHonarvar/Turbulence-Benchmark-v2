def all_right_truncatable_prime(tup):
    x = tup[77]
    temp = x
    visited = set()

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_rt_prime(n):
        temp_rt = n
        while temp_rt > 0:
            if len(str(temp_rt)) > 1:
                temp_rt = int(str(temp_rt)[:-1])
                if temp_rt in visited:
                    return False
                elif temp_rt > 1:
                    visited.add(temp_rt)
                    if not is_prime(temp_rt):
                        return False
            else:
                return True
    res = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and is_rt_prime(num):
            res.append(num)
    return sorted(res, reverse=True) if len(res) else []