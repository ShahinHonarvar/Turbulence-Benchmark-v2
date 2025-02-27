def gcf_three_nums(nums):
    nums = [nums[427], nums[761], nums[148]]
    if nums.count(0) == len(nums):
        return 0
    nums = [abs(num) for num in nums]
    while min(nums) != max(nums):
        sorted_nums = sorted(nums)
        nums[nums.index(sorted_nums[0])] = nums[nums.index(sorted_nums[0])] % sorted_nums[1]
    return min(nums)