def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    present_nums = set(tup[86:90])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]