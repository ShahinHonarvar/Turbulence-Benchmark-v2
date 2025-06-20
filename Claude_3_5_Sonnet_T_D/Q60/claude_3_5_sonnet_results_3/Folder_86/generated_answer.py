def all_left_right_truncatable_prime(numbers):

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
            if not is_prime(int(num)):
                return False
            num = num[1:-1]
        return is_prime(int(num))
    x = numbers[126]
    result = []
    for num in range(x, 10, -1):
        if is_left_right_truncatable(num):
            result.append(num)
    return result