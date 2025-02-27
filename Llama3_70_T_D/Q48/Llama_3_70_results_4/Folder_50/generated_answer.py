def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    missing_nums = [i for i in range(a + 1, b) if i not in tup[13:77]]
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]