def return_binary_or_hexa(tup):
    sum = 0
    for i in range(57, 85):
        if i not in tup:
            sum += i + 1
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].lower()