def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:len(str_n) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = nums[61]
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num) and '0' not in str(num):
            result.append(num)
    return sorted(result)