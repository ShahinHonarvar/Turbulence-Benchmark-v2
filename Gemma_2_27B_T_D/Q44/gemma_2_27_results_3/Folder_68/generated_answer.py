def composite_nums_between_indices(nums):
    result = set()
    for i in range(9):
        if i >= 0 and i <= 8:
            n = nums[i]
            if n > 1:
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        result.add(n)
                        break
    return result