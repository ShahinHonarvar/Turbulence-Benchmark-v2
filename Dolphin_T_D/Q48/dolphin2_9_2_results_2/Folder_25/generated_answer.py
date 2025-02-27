def return_binary_or_hexa(data):
    a = data[37]
    b = data[43]
    data_range = data[38:43]
    sum_range = sum(range(a + 1, b))
    sum_not_in_data = sum_range - sum(data_range)
    if all((i in data_range for i in range(a + 1, b))):
        return ''
    else:
        return bin(sum_not_in_data)[2:] if sum_not_in_data % 2 != 0 else hex(sum_not_in_data)[2:]