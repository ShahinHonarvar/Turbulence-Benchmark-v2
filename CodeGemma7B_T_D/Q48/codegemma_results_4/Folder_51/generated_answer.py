def return_binary_or_hexa(t):
    lower, upper = (t[6], t[9])
    number_set = {num for num in range(lower + 1, upper)}
    missing_numbers = number_set - set(t[6:10])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()