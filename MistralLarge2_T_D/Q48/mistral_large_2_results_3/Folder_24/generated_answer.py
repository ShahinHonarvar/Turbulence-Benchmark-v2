def return_binary_or_hexa(t):
    a, b = (t[13], t[91])
    nums = set(range(a + 1, b)) - set(t[13:92])
    sum_nums = sum(nums)
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:]
    return ''