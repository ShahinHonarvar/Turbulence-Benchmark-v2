def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:80])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    elif sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()