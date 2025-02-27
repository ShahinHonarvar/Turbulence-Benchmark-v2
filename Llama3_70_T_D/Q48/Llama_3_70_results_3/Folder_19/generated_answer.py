def return_binary_or_hexa(tup):
    a, _, _, _, b, *_ = tup
    sum_odd = sum((i for i in range(a + 1, b) if i not in tup[1:5]))
    return bin(sum_odd)[2:] if sum_odd % 2 else hex(sum_odd)[2:]