def return_binary_or_hexa(numbers):
    a, b = (numbers[6], numbers[9])
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in numbers[6:10]))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()