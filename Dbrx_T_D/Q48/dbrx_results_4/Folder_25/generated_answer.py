def return_binary_or_hexa(tup):
    a, b = (tup[37], tup[43])
    present_set = set(tup[37:44])
    absent_nums = set(range(a + 1, b))
    absent_nums -= present_set
    if not absent_nums:
        return ''
    sum_of_absent_nums = sum(absent_nums)
    if sum_of_absent_nums % 2:
        return bin(sum_of_absent_nums)[2:]
    else:
        return hex(sum_of_absent_nums)