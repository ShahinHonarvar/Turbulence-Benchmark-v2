def all_right_truncatable_prime(tup):
    x = tup[100]
    result = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = int(str(temp)[:-1])
        return True
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)[::-1]