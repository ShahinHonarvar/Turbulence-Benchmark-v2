def return_binary_or_hexa(tuple_):
    a = tuple_[200]
    b = tuple_[202]
    missing = [i for i in range(a + 1, b) if i not in tuple_[200:203]]
    if sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:]