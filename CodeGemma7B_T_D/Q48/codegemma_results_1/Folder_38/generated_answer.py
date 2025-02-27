def return_binary_or_hexa(sorted_tuple):
    sum = 0
    for i in range(sorted_tuple[36] + 1, sorted_tuple[85]):
        if i not in sorted_tuple[36:85]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]