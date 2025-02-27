def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    missing_nums = [i for i in range(a + 1, b) if i not in tup[1:5]]
    total = sum(missing_nums)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]