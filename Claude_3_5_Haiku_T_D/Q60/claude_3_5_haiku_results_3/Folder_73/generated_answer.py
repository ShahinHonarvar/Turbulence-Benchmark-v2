def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    result = []

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                return False
        return is_prime(num)
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    return sorted(result)