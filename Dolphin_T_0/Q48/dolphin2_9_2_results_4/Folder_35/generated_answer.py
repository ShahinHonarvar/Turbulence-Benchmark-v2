def return_binary_or_hexa(input_tuple):
    a = input_tuple[77]
    b = input_tuple[84]
    sum_num = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_num += i
    if sum_num % 2 != 0:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]