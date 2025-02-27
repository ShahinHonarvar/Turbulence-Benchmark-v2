def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for num in list_of_nums:
        if num >= 59 and num <= 97 and (not num % 2):
            composite_nums.add(num)
    return composite_nums