def composite_nums_between_indices(nums):
    composites = set()
    for i in range(62, 100):
        if i < len(nums):
            num = nums[i]
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composites.add(num)
                        break
                else:
                    continue
    return composites