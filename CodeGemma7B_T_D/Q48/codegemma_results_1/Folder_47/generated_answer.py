def return_binary_or_hexa(Tuple):
    a, b = (Tuple[29], Tuple[53])
    SumOfNumbers = sum((x for x in range(a + 1, b) if x not in Tuple[29:54]))
    if SumOfNumbers % 2:
        return bin(SumOfNumbers)[2:]
    else:
        return hex(SumOfNumbers)[2:].upper()