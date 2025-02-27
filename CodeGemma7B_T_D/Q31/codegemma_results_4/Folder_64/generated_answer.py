def if_perfect_num(nums):
    for num in nums:
        if num == 1 or num == 2:
            continue
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                break
        else:
            if num == nums[1]:
                return True
    return False