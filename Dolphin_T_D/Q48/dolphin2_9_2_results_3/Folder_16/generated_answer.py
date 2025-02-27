def return_binary_or_hexa(tupl):
    a = tupl[90]
    b = tupl[97]
    missing_nums = [num for num in range(a + 1, b) if num not in tupl]
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]