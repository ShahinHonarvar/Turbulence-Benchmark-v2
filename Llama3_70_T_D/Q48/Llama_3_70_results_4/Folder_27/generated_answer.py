def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    nums = set(tup[86:90])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]