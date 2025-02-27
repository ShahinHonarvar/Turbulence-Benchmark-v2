def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[0:5]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums