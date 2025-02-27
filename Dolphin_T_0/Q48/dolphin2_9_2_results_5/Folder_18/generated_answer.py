def return_binary_or_hexa(integers):
    a = integers[56]
    b = integers[90]
    possible_integers = set(range(a + 1, b))
    present_integers = set(integers[57:91])
    missing_integers = possible_integers - present_integers
    sum_of_integers = sum(missing_integers)
    if not missing_integers:
        return ''
    elif sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]