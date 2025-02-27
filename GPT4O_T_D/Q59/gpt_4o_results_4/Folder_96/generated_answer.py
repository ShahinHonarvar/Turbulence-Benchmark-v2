def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    x = numbers[29]
    result = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            result.append(number)
    return result