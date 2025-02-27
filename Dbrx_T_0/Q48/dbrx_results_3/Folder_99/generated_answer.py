def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[427:670])
    missing_and_present = missing_numbers - present_numbers
    if not missing_and_present:
        return ''
    sum_of_missing = sum(missing_and_present)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()