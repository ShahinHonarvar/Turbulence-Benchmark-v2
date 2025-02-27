def composite_nums_between_indices(list_of_nums):
    composite_numbers = {num for num in list_of_nums[5:8] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_numbers