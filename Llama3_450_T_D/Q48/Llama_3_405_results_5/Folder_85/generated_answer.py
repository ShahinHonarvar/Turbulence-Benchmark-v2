def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    missing_nums = [i for i in range(a + 1, b) if i not in t[1:8]]
    total = sum(missing_nums)
    if not missing_nums:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]