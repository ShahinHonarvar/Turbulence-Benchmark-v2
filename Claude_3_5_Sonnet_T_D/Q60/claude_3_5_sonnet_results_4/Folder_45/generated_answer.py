def all_left_right_truncatable_prime(tuple_of_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num = str(n)
        while len(num) > 1:
            if not is_prime(int(num[:-1])) or not is_prime(int(num[1:])):
                return False
            num = num[1:-1]
        return True
    x = tuple_of_integers[61]
    result = []
    for num in range(11, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result