def all_left_right_truncatable_prime(numbers):
    x = numbers[64]

    def is_truncatable_prime(num):
        if num <= 1:
            return False
        if '0' in str(num):
            return False
        if num in [2, 3, 5, 7]:
            return True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not (int(str_num[i:]) in [2, 3, 5, 7] or (int(str_num[i:]) > 1 and all((int(str_num[i:]) % j for j in range(2, int(int(str_num[i:]) ** 0.5) + 1))))):
                return False
            if not (int(str_num[:-i]) in [2, 3, 5, 7] or (int(str_num[:-i]) > 1 and all((int(str_num[:-i]) % j for j in range(2, int(int(str_num[:-i]) ** 0.5) + 1))))):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result