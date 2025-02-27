def composite_nums_between_indices(nums):
    output = set()
    for i in range(28, 39):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    output.add(nums[i])
                    break
    return output