def all_left_truncatable_prime(tup):
    x = tup[784]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)