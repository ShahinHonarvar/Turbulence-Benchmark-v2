def return_binary_or_hexa(tup):
    sum_ = 0
    for i in range(tup[32] + 1, tup[44]):
        if i not in tup[32:44]:
            sum_ += i
    if sum_ % 2:
        return bin(sum_)[2:]
    return hex(sum_)[2:].upper()