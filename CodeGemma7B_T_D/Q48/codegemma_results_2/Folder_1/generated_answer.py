def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[17]
    b = integer_tuple[88]
    present_nums = set(integer_tuple[17:89])
    sum = 0
    for num in range(a + 1, b):
        if num not in present_nums:
            sum += num
    if sum & 1:
        return format(sum, 'b')
    else:
        return format(sum, 'x')