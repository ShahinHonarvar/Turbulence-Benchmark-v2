def composite_nums_between_indices(nums):
    composite_nums = set()
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        if 68 <= count <= 86:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_nums.add(num)
        count += 1
    return composite_nums