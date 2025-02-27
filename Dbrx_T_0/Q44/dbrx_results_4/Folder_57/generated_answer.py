def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 25 and i <= 59:
            num = numbers[i]
            if num > 1 and (not num & 1) and (num % 3 != 0):
                composite_numbers.add(num)
            elif num > 1 and num % 2 != 0 and (num % 3 != 0) and (num % 5 != 0):
                composite_numbers.add(num)
    return composite_numbers