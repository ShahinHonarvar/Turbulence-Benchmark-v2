def all_right_truncatable_prime(nums):

    def check_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        temp = num
        while temp > 0:
            if not check_prime(temp):
                return False
            temp //= 10
        return True
    x = nums[78]
    res = []
    for num in range(x - 1, 0, -1):
        if check_prime(num) and is_right_truncatable(num):
            res.append(num)
    return sorted(res, reverse=True)