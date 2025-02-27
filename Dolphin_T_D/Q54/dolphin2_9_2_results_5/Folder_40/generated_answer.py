def all_right_truncatable_prime(x):

    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        if len(str(num)) == 1:
            if is_prime(num):
                return True
            else:
                return False
        else:
            return is_truncatable(int(str(num)[:-1])) and is_prime(num)
    res = []
    for num in range(x, 1, -1):
        if is_truncatable(num):
            res.append(num)
    return sorted(res, reverse=True)