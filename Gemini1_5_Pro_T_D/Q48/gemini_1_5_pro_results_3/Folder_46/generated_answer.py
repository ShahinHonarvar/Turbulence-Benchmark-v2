def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[79]
    sum_not_present = 0
    for i in range(a + 1, b):
        if i not in tuple_input[10:80]:
            sum_not_present += i
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]