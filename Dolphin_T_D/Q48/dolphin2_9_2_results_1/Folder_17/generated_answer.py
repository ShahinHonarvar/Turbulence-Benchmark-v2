def return_binary_or_hexa(tuples):
    a = tuples[73]
    b = tuples[84]
    numbers = set(range(a + 1, b))
    tuples_range = set(tuples[74:84])
    sum = numbers.symmetric_difference(tuples_range)
    sum = sum(sum)
    if sum % 2 == 0:
        return str(hex(sum))[2:]
    else:
        return str(bin(sum))[2:]