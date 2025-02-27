def return_binary_or_hexa(lst):
    a, b = (lst[10], lst[79])
    missing_nums = [x for x in range(a + 1, b) if x not in lst]
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()