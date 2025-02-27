def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in numbers[20:52]))
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]