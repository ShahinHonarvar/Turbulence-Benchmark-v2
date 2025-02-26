def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    missing_nums = [num for num in range(a + 1, b) if num not in tup[44:68]]
    if not missing_nums:
        return ''
    missing_sum = sum(missing_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]