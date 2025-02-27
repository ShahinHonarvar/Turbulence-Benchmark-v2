def all_right_truncatable_prime(t):

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        if not is_prime(num):
            return False
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[:-i])):
                return False
        return True
    x = t[992]
    right_truncatables = []
    for num in range(x):
        if is_right_truncatable(num):
            right_truncatables.append(num)
    return sorted(right_truncatables)