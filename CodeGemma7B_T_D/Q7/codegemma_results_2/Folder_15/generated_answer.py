def all_even_ints_inclusive(nums):
    result = []
    for i in range(0, len(nums) - 2):
        if nums[i] % 2 == 0:
            if nums[i + 1] % 2 == 0:
                if nums[i + 2] % 2 == 0:
                    result.append(nums[i])
                    result.append(nums[i + 1])
                    result.append(nums[i + 2])
    return result