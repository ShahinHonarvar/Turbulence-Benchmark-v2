def composite_nums_between_indices(nums):
    if len(nums) < 83:
        return set()
    composite_numbers = set()
    for i in range(56, 83):
        num = nums[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            composite_numbers.add(num)
        elif num > 3:
            for j in range(5, int(num ** 0.5) + 1, 6):
                if num % j == 0 or num % (j + 2) == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers