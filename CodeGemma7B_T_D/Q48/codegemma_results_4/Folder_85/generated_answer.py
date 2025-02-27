def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[1:9]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        hex_sum = hex(sum)[2:]
        hex_sum = hex_sum.upper() if hex_sum.islower() else hex_sum.lower()
        return hex_sum