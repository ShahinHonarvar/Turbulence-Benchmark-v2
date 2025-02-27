def composite_nums_between_indices(nums):
    composite_nums = set()
    if len(nums) > 50 and len(nums) <= 200:
        for i in range(50, 201):
            num = nums[i]
            if num > 1 and num % 2 != 0 and (num % 3 != 0):
                for j in range(5, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composite_nums.add(num)
                        break
    return composite_nums