def if_perfect_num(nums):
    total = 1
    for i in range(2, int(nums[45] ** 0.5) + 1):
        if nums[45] % i == 0:
            total += i + nums[45] // i
    return total == nums[45]