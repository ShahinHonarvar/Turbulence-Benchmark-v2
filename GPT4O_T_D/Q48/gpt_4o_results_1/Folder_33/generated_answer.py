def return_binary_or_hexa(integers_tuple):
    if len(integers_tuple) <= 35:
        return ''
    a = integers_tuple[13]
    b = integers_tuple[35]
    missing_sum = sum((i for i in range(a + 1, b) if i not in integers_tuple[14:35]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]