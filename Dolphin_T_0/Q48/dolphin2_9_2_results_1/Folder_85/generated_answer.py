def return_binary_or_hexa(tuple_):
    a, b = (tuple_[1], tuple_[8])
    missing_numbers = [x for x in range(a + 1, b) if x not in tuple_[1:8]]
    sum_missing_numbers = sum(missing_numbers)
    if missing_numbers == []:
        return ''
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:].upper()
    else:
        return bin(sum_missing_numbers)[2:]