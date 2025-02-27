def all_neg_ints_exclusive(nums):
    nums.reverse()
    result = []
    for i in range(len(nums)):
        if -93 <= abs(nums[i]) < 51:
            result.append(nums[i])
        elif abs(nums[i]) >= 93:
            break
    return result[::-1]