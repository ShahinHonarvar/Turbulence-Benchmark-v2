def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[42]
    b = tuple_of_integers[87]
    sum_of_integers = 0
    for number in tuple_of_integers:
        if a + 1 <= number <= b - 1 and number != a and (number != b):
            sum_of_integers += number
    if sum_of_integers == 0 or a + 1 == b:
        return ''
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].upper()
    else:
        return bin(sum_of_integers)[2:]