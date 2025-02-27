def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        trunc_len = len(str_n)
        for i in range(trunc_len):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:trunc_len - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = nums[175]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return result