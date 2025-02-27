def all_left_truncatable_prime(tup):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def left_truncatable(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = tup[38]
    result = []
    for num in range(2, x):
        if is_prime(num) and left_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)