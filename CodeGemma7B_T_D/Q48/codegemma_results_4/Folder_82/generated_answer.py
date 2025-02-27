def return_binary_or_hexa(num_tuple):
    sum = 0
    for n in range(num_tuple[20] + 1, num_tuple[200] + 1):
        if n not in num_tuple[20:200]:
            sum += n
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()