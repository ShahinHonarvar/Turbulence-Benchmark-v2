def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(n):
    x = n[29]
    res = [2, 3, 5, 7]
    for num in range(11, x):
        if is_prime(num):
            tem = num
            while tem != 0:
                tem //= 10
                if not is_prime(tem):
                    break
            else:
                res.append(num)
    return sorted(res)