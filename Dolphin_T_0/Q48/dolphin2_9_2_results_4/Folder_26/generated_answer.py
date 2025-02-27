def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    if all((i in t[69:99] for i in range(a + 1, b))):
        return ''
    else:
        result = sum((i for i in range(a + 1, b) if i not in t))
        if result % 2 == 0:
            return bin(result)[2:]
        else:
            return hex(result)[2:]