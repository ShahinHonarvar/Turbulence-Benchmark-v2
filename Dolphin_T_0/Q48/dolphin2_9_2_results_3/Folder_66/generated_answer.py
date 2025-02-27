def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[12:76]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]