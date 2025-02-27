def return_binary_or_hexa(a_b_tuple):
    a, b = (a_b_tuple[450], a_b_tuple[905])
    sum = 0
    for i in range(a + 1, b):
        if i not in a_b_tuple[450:905]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()