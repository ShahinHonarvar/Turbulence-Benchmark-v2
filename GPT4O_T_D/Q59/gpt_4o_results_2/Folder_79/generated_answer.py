def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    if len(nums) <= 91:
        return []
    x = nums[91]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return result