def return_binary_or_hexa(tup):
    sum = 0
    for i in range(17, 88):
        if i not in tup:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:]