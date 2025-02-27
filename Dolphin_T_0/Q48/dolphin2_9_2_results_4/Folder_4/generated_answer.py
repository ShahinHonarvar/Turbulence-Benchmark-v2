def return_binary_or_hexa(lst):
    a = lst[49]
    b = lst[74]
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - set(lst[50:74])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]