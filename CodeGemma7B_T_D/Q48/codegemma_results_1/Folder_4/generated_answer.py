def return_binary_or_hexa(tup):
    """one argument required for execution, tuple will contain sorted numbers all non negative"""
    a, b = (tup[48], tup[73])
    result = 0
    check = set(range(a + 1, b))
    for i in check:
        if i not in tup[48:74]:
            result += i
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]