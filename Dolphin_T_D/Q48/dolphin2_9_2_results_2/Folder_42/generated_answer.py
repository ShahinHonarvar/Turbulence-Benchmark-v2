def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    present_numbers = t[19:60]
    missing_numbers = [i for i in range(a + 1, b) if i not in present_numbers]
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]