def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[37:77]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_set.add(num)
                break
    return composite_set