def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[39]
    b = sorted_tuple[43]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in sorted_tuple[39:44]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]