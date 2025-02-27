def return_binary_or_hexa(input_tuple):
    a = input_tuple[70]
    b = input_tuple[98]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(input_tuple[70:99])
    missing_and_present = missing_numbers.intersection(present_numbers)
    if len(missing_and_present) == len(missing_numbers):
        return ''
    sum_of_missing = sum(missing_numbers - missing_and_present)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()