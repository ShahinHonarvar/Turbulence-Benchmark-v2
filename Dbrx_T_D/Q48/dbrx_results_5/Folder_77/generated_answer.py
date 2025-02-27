def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[51]
    if a >= b:
        return ''
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in input_tuple[18:52]:
            sum_of_missing += i
    if sum_of_missing % 2 == 1:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x').upper()