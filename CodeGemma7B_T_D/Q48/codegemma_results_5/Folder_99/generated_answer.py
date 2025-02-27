def return_binary_or_hexa(tuple):
    maximum = tuple[669]
    minimum = tuple[427]
    answer = 0
    for i in range(minimum + 1, maximum):
        if i not in tuple[427:670]:
            answer += i
    if answer % 2 == 1:
        return bin(answer)[2:]
    else:
        return hex(answer)[2:].upper()