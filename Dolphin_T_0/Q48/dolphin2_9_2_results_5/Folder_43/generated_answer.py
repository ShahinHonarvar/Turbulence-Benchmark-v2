def return_binary_or_hexa(num_tuple):
    a = num_tuple[10]
    b = num_tuple[28]
    sub_tuple = num_tuple[11:29]
    sum = 0
    for i in range(a + 1, b):
        if i not in sub_tuple:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]