def return_binary_or_hexa(t):
    for i in range(28, 97):
        if i not in t:
            s = s + i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]