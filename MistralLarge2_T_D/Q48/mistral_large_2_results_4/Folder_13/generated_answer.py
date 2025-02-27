def return_binary_or_hexa(data):
    a = data[46]
    b = data[91]
    subset = set(data[46:92])
    sum_value = sum((x for x in range(a + 1, b) if x not in subset))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]