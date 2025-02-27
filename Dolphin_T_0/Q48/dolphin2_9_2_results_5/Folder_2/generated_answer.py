def return_binary_or_hexa(tuple):
    a = tuple[72]
    b = tuple[93]
    numbers_to_use = [num for num in range(a + 1, b) if num not in tuple[72:93 + 1]]
    sum_of_numbers = sum(numbers_to_use)
    if sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)[2:]
    else:
        return bin(sum_of_numbers)[2:]