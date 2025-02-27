def composite_nums_between_indices(nums):
    composite_set = set()
    if len(nums) < 87:
        return composite_set
    for i in range(51, 87):
        num = nums[i]
        if num > 1 and (not num & 1) and (num % 3 != 0) or (num > 3 and any((num % j == 0 for j in range(4, int(num ** 0.5) + 1, 2)))):
            composite_set.add(num)
    return composite_set