def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    missing_nums = set(range(a + 1, b)) - set(t[10:12])
    if len(missing_nums) == 0:
        return ''
    else:
        Sum = sum(missing_nums)
        if Sum % 2 == 1:
            return bin(Sum)[2:]
        else:
            return hex(Sum)[2:]