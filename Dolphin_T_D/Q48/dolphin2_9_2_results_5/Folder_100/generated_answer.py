def return_binary_or_hexa(int_tuple):
    a = int_tuple[44]
    b = int_tuple[78]
    sum_included = 0
    for num in int_tuple[45:78]:
        sum_included += num
    if sum_included == b - a - 2:
        return ''
    else:
        sum_excluded = sum(range(a + 1, b)) - sum_included
        if sum_excluded % 2 == 0:
            return hex(sum_excluded)[2:]
        else:
            return bin(sum_excluded)[2:]