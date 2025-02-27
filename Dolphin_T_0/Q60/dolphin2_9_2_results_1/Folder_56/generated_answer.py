def all_left_right_truncatable_prime(tup):

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
    x = tup[30]
    result = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        i = 1
        while i < len(str_num):
            if not is_prime(int(str_num[i:])):
                break
            i += 1
            if not is_prime(int(str_num[:i])):
                break
        if i == len(str_num):
            result.append(num)
    return sorted(result)