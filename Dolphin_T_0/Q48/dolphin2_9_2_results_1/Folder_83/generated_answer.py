def return_binary_or_hexa(t):
    a = t[90]
    b = t[200]
    nums_between = {i for i in range(a + 1, b)}
    if nums_between.issubset(t):
        return ''
    sum_nums = sum(nums_between - set(t[91:200]))
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]