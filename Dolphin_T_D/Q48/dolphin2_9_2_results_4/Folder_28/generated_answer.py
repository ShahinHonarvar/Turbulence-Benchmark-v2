def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    nums = list(range(a + 1, b))
    for i in range(86, 100):
        if t[i] in nums:
            nums.remove(t[i])
    s = sum(nums)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]