def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 70 and i <= 84:
            num = numbers[i]
            if num > 1 and (not num & 1):
                composite_numbers.add(num)
    return composite_numbers