def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[10]
    b = numbers_tuple[79]
    sum_numbers = 0
    for i in range(a + 1, b):
        if numbers_tuple.index(i) < 10 or numbers_tuple.index(i) > 79:
            sum_numbers += i
    binary_sum = bin(sum_numbers)[2:]
    if int(binary_sum, 2) % 2 == 0:
        return hex(sum_numbers).split('x')[-1].upper()
    else:
        return binary_sum