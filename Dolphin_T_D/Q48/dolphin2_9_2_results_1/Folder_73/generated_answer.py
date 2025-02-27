def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    missing_numbers = set(range(a + 1, b)) - set(numbers[11:76])
    if missing_numbers:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2 == 0:
            return hex(sum_of_missing_numbers)[2:]
        else:
            return bin(sum_of_missing_numbers)[2:]
    else:
        return ''