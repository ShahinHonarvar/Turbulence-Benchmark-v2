def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    all_numbers = set(range(a + 1, b))
    tuple_numbers = set(t[1:6])
    missing_numbers = all_numbers - tuple_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].rstrip('L')