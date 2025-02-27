def return_binary_or_hexa(num_tuple):
    sum = 0
    for i in range(num_tuple[60] + 1, num_tuple[200]):
        if i not in num_tuple[60:201]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()