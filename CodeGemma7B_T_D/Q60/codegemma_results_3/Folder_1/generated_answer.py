def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                break
        else:
            result.append(num)
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:-i])):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)