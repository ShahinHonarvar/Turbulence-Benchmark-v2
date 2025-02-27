def all_left_right_truncatable_prime(tup):
    x = tup[23]

    def is_prime(num):
        return num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    res = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            left, right = (i, i)
            while left > 1 or right > 1:
                if is_prime(left) and is_prime(right):
                    res.append(i)
                    break
                left = left // 10
                right = int(str(right)[1:])
    return sorted(res)