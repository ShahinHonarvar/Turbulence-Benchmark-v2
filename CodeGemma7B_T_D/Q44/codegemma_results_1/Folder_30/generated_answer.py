def composite_nums_between_indices(input_list: list):
    if len(input_list) == 0 or not all((isinstance(num, int) and num > 0 for num in input_list)):
        return set()
    nums_in_range = [num for num in input_list if num >= 19 and num <= 92]
    composite_nums = set()
    for num in nums_in_range:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums