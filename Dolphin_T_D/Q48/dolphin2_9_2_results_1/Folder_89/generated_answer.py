def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    present_numbers = [x for x in numbers if a < x < b]
    missing_numbers = [x for x in range(a + 1, b) if x not in present_numbers]
    sum_of_missing = sum(missing_numbers)
    if len(missing_numbers) == 0:
        return ''
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]