def all_left_right_truncatable_prime(tuple_input):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num = str(n)
        while len(num) > 1:
            num = num[1:-1]
            if not is_prime(int(num)):
                return False
        return True
    x = tuple_input[803]
    result = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result