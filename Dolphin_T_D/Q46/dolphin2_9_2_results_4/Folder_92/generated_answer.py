def gcf_three_nums(nums):
    nums = nums[::-1]
    a = nums[7]
    b = nums[9]
    nums = nums[10:]
    return_nums = []
    for i in range(len(nums)):
        if i == 0:
            c = nums[i]
        elif nums[i] % a == 0 and nums[i] % b == 0 and (nums[i] % c == 0):
            return_nums.append(nums[i])
    if len(return_nums) != 0:
        return max(return_nums)
    else:
        return 'No common factor'