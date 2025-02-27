def composite_nums_between_indices(numbers):
    composite_nums = set()
    for index, num in enumerate(numbers):
        if index >= 20 and index <= 200:
            if num > 1 and (not num & 1):
                composite_nums.add(num)
    return composite_nums