def return_binary_or_hexa(int_tuple: tuple) -> str:
    sum = 0
    for i in range(21, 37):
        if int_tuple[i] not in range(int_tuple[20] + 1, int_tuple[36] + 1):
            sum += int_tuple[i]
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()