def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    missing_nums = [i for i in range(a + 1, b) if i not in tup[44:92]]
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]