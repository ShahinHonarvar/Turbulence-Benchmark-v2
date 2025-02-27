def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    missing_numbers = set(range(a + 1, b)) - set(numbers[1:7])
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]