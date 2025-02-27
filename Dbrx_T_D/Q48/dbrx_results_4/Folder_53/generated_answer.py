def return_binary_or_hexa(tup):
    a = tup[200]
    b = tup[202]
    sum = 0
    present = [i for i in range(a + 1, b) if i in tup[200:203]]
    if len(present) != b - a - 1:
        for i in range(a + 1, b):
            if i not in present:
                sum += i
        if sum % 2 != 0:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:].upper()
    else:
        return ''