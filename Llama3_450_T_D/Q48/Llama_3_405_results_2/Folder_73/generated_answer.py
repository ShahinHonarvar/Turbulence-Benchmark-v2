def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[76])
    absent_nums = [num for num in range(a + 1, b) if num not in tup[10:76]]
    total = sum(absent_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]