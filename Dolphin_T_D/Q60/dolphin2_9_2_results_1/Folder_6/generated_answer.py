def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 2:
            return False
        nums = [int(d) for d in str(n)]
        while len(nums) > 1:
            if not is_prime(int(''.join(map(str, nums)))):
                return False
            if numbers[-1] == 0:
                return False
            if not is_prime(int(''.join(map(str, nums[1:]))) and (not is_prime(int(''.join(map(str, nums[:-1])))))):
                return False
            nums = nums[1:-1]
        return True
    x = t[74]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)])