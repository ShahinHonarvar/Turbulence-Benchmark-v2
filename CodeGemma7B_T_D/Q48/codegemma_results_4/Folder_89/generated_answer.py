def return_binary_or_hexa(tup):
    """Return the binary or hexadecimal representation of the sum of the integers in the tuple from a+1 to b-1."""
    a = tup[55]
    b = tup[84]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in tup[55:85]:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()