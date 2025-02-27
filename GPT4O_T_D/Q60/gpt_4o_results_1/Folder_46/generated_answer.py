def all_left_right_truncatable_prime(numbers):
    x = numbers[33]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        if '0' in str_n:
            return False
        for i in range(length):
            left_truncate_num = int(str_n[i:])
            right_truncate_num = int(str_n[:length - i])
            if not is_prime(left_truncate_num) or not is_prime(right_truncate_num):
                return False
        return True
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result