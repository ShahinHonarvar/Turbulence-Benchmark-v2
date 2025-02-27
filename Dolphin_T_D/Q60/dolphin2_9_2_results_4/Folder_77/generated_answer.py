def all_left_right_truncatable_prime(nums):

    def check_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        while len(num_str) > 1:
            if not is_prime(int(num_str[1:-1])):
                return False
            num_str = num_str[1:-1]
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([num for num in range(2, nums[767] + 1) if is_prime(num) and check_truncatable(num)], reverse=True)