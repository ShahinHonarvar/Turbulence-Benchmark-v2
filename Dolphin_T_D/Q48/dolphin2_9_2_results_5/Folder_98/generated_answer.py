def return_binary_or_hexa(tup):
    a = tup[6]
    b = tup[7]
    missing_nums = [i for i in range(a + 1, b) if i not in tup]
    if len(missing_nums) == 0:
        return ''
    elif sum(missing_nums) % 2 == 1:
        return bin(sum(missing_nums))[2:]
    else:
        return hex(sum(missing_nums))[2:].upper()