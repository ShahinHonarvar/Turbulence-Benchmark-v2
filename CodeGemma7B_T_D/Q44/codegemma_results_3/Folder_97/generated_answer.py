def composite_nums_between_indices(nums):
    composites = set()
    for i in range(15, 40):
        if not (nums[i] == 2 or nums[i] == 3):
            flag = True
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    flag = False
                    break
            composites |= {nums[i]} if flag else set()
    return composites