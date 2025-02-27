def return_binary_or_hexa(numbers):
    a, b = (numbers[49], numbers[74])
    elements_between = set(range(a + 1, b))
    missing_elements = elements_between - set(numbers[50:74])
    if not missing_elements:
        return ''
    sum_missing = sum(missing_elements)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]