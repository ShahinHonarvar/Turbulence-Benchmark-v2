def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    total_sum = 0
    for i in range(a + 1, b):
        total_sum += i
        if i in t[6:10]:
            total_sum -= i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]