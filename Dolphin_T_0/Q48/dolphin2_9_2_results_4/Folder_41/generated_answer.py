def return_binary_or_hexa(integers):
    a = integers[3]
    b = integers[8]
    missing_nums = [i for i in range(a + 1, b) if i not in integers]
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]