def return_binary_or_hexa(lst):
    a = lst[34]
    b = lst[69]
    present = set(lst[35:69])
    missing = [x for x in range(a + 1, b) if x not in present]
    result_sum = sum(missing)
    if result_sum % 2:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:].upper()