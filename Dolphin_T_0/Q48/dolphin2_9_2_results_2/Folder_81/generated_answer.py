def return_binary_or_hexa(tuples):
    a = tuples[10]
    b = tuples[100]
    present = [False] * (b - a + 1)
    for num in tuples:
        if a + 1 <= num <= b - 1:
            present[num - (a + 1)] = True
    summ = sum([num for num in range(a + 1, b + 1) if not present[num - (a + 1)]])
    if summ % 2 != 0:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:]