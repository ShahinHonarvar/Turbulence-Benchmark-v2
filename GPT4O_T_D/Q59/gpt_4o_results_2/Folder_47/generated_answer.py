def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncate(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    x = numbers[49]
    result = []
    for number in range(2, x):
        if '0' not in str(number) and is_prime(number) and left_truncate(number):
            result.append(number)
    return sorted(result)