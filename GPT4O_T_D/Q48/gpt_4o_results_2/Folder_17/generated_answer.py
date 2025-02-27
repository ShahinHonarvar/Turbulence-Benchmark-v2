def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    required_sum = sum((i for i in range(a + 1, b) if i not in t[74:84]))
    if a + 1 == b or required_sum == 0:
        return ''
    if required_sum % 2 == 1:
        return bin(required_sum)[2:]
    else:
        return hex(required_sum)[2:]