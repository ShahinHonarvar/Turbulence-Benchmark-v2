def return_binary_or_hexa(tp):
    bin_sum = 0
    for i in range(tp[2] + 1, tp[7]):
        if i not in tp:
            bin_sum += i
    if bin_sum % 2 == 1:
        return bin_sum.__str__()
    else:
        return hex(bin_sum)[2:].upper()