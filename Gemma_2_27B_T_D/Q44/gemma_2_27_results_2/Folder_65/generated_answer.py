def composite_nums_between_indices(nums):
    composites = set()
    for i in range(82, 87):
        if i < len(nums):
            num = nums[i]
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composites.add(num)
                        break
    return composites