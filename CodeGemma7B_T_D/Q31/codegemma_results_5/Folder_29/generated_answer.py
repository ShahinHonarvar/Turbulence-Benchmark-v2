def if_perfect_num(nums):
    for num in nums:
        if num == nums[19]:
            factors = 0
            for i in range(1, num):
                if num % i == 0:
                    factors += i
            if factors == num:
                return True
    return False