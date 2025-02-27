def composite_nums_between_indices(nums):
    composites = set()
    if not nums or len(nums) < 3:
        return composites
    for i in range(len(nums)):
        if nums[i] > 1 and all((j % nums[i] != 0 for j in range(2, nums[i]))):
            composites.add(nums[i])
    return composites & {num for num in nums if 0 <= nums.index(num) <= 2}