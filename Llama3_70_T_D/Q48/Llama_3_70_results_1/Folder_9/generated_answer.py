def return_binary_or_hexa(tup):
    a, b = (tup[70], tup[200])
    full_range = set(range(a + 1, b))
    tup_range = set(tup[71:201])
    missing_nums = full_range - tup_range
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]