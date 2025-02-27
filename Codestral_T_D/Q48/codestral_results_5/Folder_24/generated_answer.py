def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[91]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[13:92]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]