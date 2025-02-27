def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 28 and i <= 40:
            num = nums[i]
            if num > 1 and (not (num == 2 or num % 2 == 0)):
                is_composite = False
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        is_composite = True
                        break
                if is_composite:
                    composite_nums.add(num)
    return composite_nums