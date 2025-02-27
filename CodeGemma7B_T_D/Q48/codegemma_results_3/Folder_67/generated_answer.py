def return_binary_or_hexa(input_tuple):
    a = input_tuple[44]
    b = input_tuple[67]
    sum_result = 0
    for number in range(a + 1, b):
        if number not in input_tuple[44:68]:
            sum_result += number
    if sum_result % 2 == 1:
        return str(bin(sum_result))[2:]
    else:
        return hex(sum_result)[2:].upper()