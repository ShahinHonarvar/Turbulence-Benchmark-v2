def return_binary_or_hexa(lst):
    a = lst[10]
    b = lst[12]
    s = set(lst[10:13])
    result_sum = sum((x for x in range(a + 1, b) if x not in s))
    if result_sum == 0:
        return ''
    elif result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]