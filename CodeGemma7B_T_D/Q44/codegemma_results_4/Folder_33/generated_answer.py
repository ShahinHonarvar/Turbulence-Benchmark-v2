def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for num in list_of_nums[314:348]:
        if num != 1 and num != 2:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums