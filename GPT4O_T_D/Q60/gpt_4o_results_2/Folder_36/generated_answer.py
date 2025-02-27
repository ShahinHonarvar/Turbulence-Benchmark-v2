def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:length - i])):
                return False
        return True
    x = numbers[992]
    result = []
    for i in range(11, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return result