def return_binary_or_hexa(tup):
    sum = 0
    num = tup[81] + 1
    while num < tup[86]:
        if num not in tup[81:86]:
            sum += num
        num += 1
    if sum % 2 == 1:
        return str(bin(sum))[2:]
    else:
        return hex(sum)[2:].upper() if sum <= 9 else hex(sum)[2:]