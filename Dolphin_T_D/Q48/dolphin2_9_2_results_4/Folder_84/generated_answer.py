def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[32]
    b = tuple_of_integers[44]
    subarray = tuple_of_integers[33:45]
    missing_numbers = [n for n in range(a + 1, b) if n not in subarray]
    result_sum = sum(missing_numbers)
    if len(missing_numbers) == 0:
        return ''
    elif result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]