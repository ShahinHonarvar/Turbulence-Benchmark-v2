def if_perfect_num(nums):
    if len(nums) > 4:
        x = nums[4]
        perfect = False
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                perfect = True
        if perfect:
            return True
    return False