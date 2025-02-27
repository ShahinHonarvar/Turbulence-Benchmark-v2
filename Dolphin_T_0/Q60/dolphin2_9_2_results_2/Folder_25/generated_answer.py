def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num = str(num)
        while len(num) > 1:
            if not is_prime(int(num)):
                return False
            num = num[1:-1]
        return True
    max_num = nums[92]
    res = [i for i in range(2, max_num + 1) if is_truncatable_prime(i)]
    return res