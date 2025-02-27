def return_binary_or_hexa(input_tuple):
    a = input_tuple[68]
    b = input_tuple[99]
    if a + 1 >= b - 1:
        return ''
    sum_result = 0
    for i in range(a + 1, b):
        if i not in input_tuple[68:100]:
            sum_result += i
    if sum_result % 2 != 0:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].upper()