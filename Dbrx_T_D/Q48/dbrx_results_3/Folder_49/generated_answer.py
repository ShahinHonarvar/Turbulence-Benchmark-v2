def return_binary_or_hexa(args):
    a = args[80]
    b = args[200]
    missing_numbers = set(range(a + 1, b)) - set(args[80:201])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()