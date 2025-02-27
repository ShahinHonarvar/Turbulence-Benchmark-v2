def all_pos_ints_inclusive(nums):
    solution = []
    for idx in range(22, 64):
        if nums[idx] > 0:
            solution.append(nums[idx])
    return solution