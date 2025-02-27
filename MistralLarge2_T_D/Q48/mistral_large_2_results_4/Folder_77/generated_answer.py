def return_binary_or_hexa(data):
    a = data[18]
    b = data[52]
    present_set = set(data[18:53])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_set))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]