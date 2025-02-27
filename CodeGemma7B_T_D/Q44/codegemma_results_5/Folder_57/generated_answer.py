def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[25:60]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and num != i:
                composite_set.add(num)
                break
    return composite_set