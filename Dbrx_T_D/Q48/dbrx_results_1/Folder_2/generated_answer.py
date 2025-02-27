def return_binary_or_hexa(arr):
    a = arr[72]
    b = arr[93]
    if a + 1 > b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(arr[72:94]) - set(range(a + 1, b))
    missing_and_present = missing_numbers - present_numbers
    if not missing_and_present:
        return ''
    sum_of_missing = sum(missing_and_present)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()