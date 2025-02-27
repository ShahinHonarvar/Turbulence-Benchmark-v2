def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i in range(31, 73):
        num = list_of_nums[i]
        if num >= 4:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums