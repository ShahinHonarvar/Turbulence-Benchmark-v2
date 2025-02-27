def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i < 686 or i > 987:
            continue
        if i >= 686 and i <= 987:
            num = nums[i]
            if num % 2 == 0 and num != 2 or (num % 3 == 0 and num != 3) or (num % 5 == 0 and num != 5):
                composite_set.add(num)
    return composite_set