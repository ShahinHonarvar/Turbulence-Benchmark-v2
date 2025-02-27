def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    s = {i for i in range(a + 1, b) if i not in t[68:100]}
    if not s:
        return ''
    sum_s = sum(s)
    return bin(sum_s)[2:] if sum_s % 2 else hex(sum_s)[2:]