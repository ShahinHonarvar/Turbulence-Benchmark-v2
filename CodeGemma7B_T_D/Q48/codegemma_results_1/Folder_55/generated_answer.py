def return_binary_or_hexa(value):
    value_list = list(value)
    a = value_list[10]
    b = value_list[12]
    max_element = max(b, max(value_list))
    result = 0
    for i in range(a + 1, b):
        if i not in value_list:
            result += i
    if result % 2 == 0:
        output = format(result, 'X')
    else:
        output = bin(result)[2:]
    return output