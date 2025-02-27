def return_binary_or_hexa(tuple):
    sum = 0
    for num in range(tuple[90] + 1, tuple[97]):
        if num not in tuple[90:97]:
            sum += num
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()