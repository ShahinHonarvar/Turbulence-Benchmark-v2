def return_binary_or_hexa(a_b_tuple):
    answer = 0
    for n in range(a_b_tuple[0] + 1, a_b_tuple[3]):
        if n not in a_b_tuple[0:4]:
            answer += n
    if answer % 2 == 1:
        return bin(answer)[2:]
    else:
        return hex(answer)[2:].upper()