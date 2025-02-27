def return_binary_or_hexa(data):
    a = data[18]
    b = data[60]
    values = data[19:60]
    total_sum = sum(range(a + 1, b)) - sum(values)
    if total_sum == 0:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]