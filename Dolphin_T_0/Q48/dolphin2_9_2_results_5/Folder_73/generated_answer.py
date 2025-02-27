def return_binary_or_hexa(input_tuple):
    a = input_tuple[10]
    b = input_tuple[76]
    missing_values = []
    for i in range(a + 1, b):
        if i not in input_tuple:
            missing_values.append(i)
    if not missing_values:
        return ''
    sum_missing_values = sum(missing_values)
    if sum_missing_values % 2 == 0:
        return hex(sum_missing_values)[2:]
    else:
        return bin(sum_missing_values)[2:]