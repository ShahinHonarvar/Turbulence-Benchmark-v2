def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    integers = range(a + 1, b)
    for number in t[29:54]:
        if number in integers:
            integers.remove(number)
    total = sum(integers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]