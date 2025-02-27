def return_binary_or_hexa(my_tuple):
    sum = 0
    for i in range(43, 88):
        if my_tuple.count(i) == 0:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]