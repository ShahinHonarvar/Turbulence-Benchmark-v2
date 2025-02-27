def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    numbers_between_a_b = [x for x in range(a + 1, b) if x not in tup[25:81]]
    if len(numbers_between_a_b) != 0:
        sum_numbers = sum(numbers_between_a_b)
        if sum_numbers % 2 == 0:
            return hex(sum_numbers)[2:].upper()
        else:
            return bin(sum_numbers)[2:]
    else:
        return ''