def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]