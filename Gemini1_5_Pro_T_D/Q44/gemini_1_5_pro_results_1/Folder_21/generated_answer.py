def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(262, 0), min(len(nums), 747)):
        num = nums[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    result.add(num)
                    break
    return result