def return_binary_or_hexa(a_b_tuple):
    sum = 0
    for i in range(a_b_tuple[450] + 1, a_b_tuple[905]):
        if i not in a_b_tuple:
            sum += i
    return '0b' + bin(sum)[2:].rjust(64, '0') if sum % 2 else '0x' + hex(sum)[2:].rjust(16, '0')