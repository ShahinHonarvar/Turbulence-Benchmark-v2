def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[73]
    b = tuple_of_ints[84]
    sum = 0
    for round_number in range(a + 1, b):
        if round_number not in tuple_of_ints:
            sum += round_number
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
    if sum == 0:
        return ''