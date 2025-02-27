def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = input_tuple[37]
    result_list = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable(i) and is_prime(i):
            result_list.append(i)
    result_list.sort(reverse=True)
    return result_list