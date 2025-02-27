def return_binary_or_hexa(input_tuple):
    a = input_tuple[13]
    b = input_tuple[70]
    s = 0
    n = len(input_tuple)
    present = set(input_tuple[13:71])
    for i in range(a + 1, b):
        if i not in present:
            s += i
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]