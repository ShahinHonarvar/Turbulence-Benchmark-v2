def composite_nums_between_indices(nums):
    composites = set()
    for i in range(len(nums)):
        if not nums[i].isdigit():
            continue
        num = int(nums[i])
        if num <= 1 or num in (4, 6, 8, 9):
            continue
        for j in range(num + 1, min(num + 4, len(nums))):
            if not nums[j].isdigit():
                continue
            composites.add(int(nums[j]))
    return composites