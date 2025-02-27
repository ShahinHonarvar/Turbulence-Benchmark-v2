def return_binary_or_hexa(tuple1):
    sum = 0
    for i in range(tuple1[0] + 1, tuple1[6]):
        if i not in tuple1:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]