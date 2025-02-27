def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[450]
    b = numbers_tuple[905]
    sum_of_elements = 0
    for i in range(a + 1, b):
        if i not in numbers_tuple[450:906]:
            sum_of_elements += i
    if sum_of_elements % 2 != 0:
        return bin(sum_of_elements)[2:]
    else:
        return hex(sum_of_elements)[2:].upper()