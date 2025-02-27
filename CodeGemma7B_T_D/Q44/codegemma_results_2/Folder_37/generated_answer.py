def composite_nums_between_indices(nums):
    composite_set = set()
    for idx, num in enumerate(nums):
        if num > 1 and all((num % i != 0 for i in range(2, idx + 1))):
            if 0 <= idx <= 5:
                composite_set.add(num)
    return composite_set