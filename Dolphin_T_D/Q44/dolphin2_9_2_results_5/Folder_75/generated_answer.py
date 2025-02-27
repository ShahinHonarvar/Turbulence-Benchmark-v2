def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(75, 86):
        number = nums[i]
        if number > 1:
            for j in range(2, number):
                if number % j == 0:
                    composite_nums.add(number)
                    break
    return composite_nums