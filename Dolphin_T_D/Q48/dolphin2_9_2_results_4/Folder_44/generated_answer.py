def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[36]
    b = tuple_of_integers[52]
    numbers_between_a_and_b = {num for num in range(a + 1, b)}
    missing_numbers = numbers_between_a_and_b - {num for num in tuple_of_integers[36:53]}
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]