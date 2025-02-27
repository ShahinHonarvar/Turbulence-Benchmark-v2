def return_binary_or_hexa(lst):
    a = lst[27]
    b = lst[96]
    missing_nums = [x for x in range(a + 1, b) if x not in lst]
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]