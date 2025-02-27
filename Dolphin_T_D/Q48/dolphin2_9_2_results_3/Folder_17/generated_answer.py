def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[73]
    b = tuple_of_integers[84]
    missing_numbers = [i for i in range(a + 1, b) if i not in tuple_of_integers[73:85]]
    if missing_numbers:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2 == 0:
            return hex(sum_of_missing_numbers)[2:]
        else:
            return bin(sum_of_missing_numbers)[2:]
    else:
        return ''