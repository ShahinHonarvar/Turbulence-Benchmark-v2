def return_binary_or_hexa(tuples):
    a = tuples[10]
    b = tuples[100]
    missing_numbers = [x for x in range(a + 1, b) if x not in tuples]
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]