def composite_nums_between_indices(nums):
    composites = set()
    for i in range(max(4, len(nums))):
        n = nums[i]
        if n > 1:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    composites.add(n)
                    break
    return composites