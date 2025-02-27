def return_binary_or_hexa(data):
    a, b = (data[86], data[90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in data[86:91]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]