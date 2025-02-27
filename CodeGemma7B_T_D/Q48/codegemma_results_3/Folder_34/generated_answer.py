def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[60:201]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    return hex(sum)[2:].lower() if sum > 15 else hex(sum).lower()[2:]