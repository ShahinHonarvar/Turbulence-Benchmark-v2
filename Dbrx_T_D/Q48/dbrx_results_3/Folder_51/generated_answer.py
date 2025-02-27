def return_binary_or_hexa(input_tuple):
    a = input_tuple[6]
    b = input_tuple[9]
    sum_of_missing = sum(range(a + 1, b)) if a + 1 <= b - 1 else 0
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x').upper() if sum_of_missing > 0 else ''