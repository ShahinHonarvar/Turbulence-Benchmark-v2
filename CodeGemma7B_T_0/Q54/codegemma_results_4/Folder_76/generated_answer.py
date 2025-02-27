def all_right_truncatable_prime(tup):
    x = tup[370]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:-i])):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)