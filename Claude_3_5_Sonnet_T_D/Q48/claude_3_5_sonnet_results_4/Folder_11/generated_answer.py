def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    all_numbers = set(range(a + 1, b))
    excluded_numbers = set(t[48:77])
    sum_of_numbers = sum(all_numbers - excluded_numbers)
    if sum_of_numbers == 0:
        return ''
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]