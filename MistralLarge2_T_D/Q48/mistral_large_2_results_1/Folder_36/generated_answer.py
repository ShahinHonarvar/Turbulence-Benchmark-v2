def return_binary_or_hexa(data):
    a = data[110]
    b = data[348]
    missing_sum = sum(set(range(a + 1, b)) - set(data[110:349]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]