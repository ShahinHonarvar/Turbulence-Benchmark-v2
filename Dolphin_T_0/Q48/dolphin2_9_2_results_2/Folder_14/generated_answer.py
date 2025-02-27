def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[5])
    missing_numbers = [num for num in range(a + 1, b) if num not in tup[2:6]]
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        if sum_missing_numbers == 0:
            return ''
        else:
            return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()