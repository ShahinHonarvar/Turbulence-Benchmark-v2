def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    if missing_numbers:
        sum_missing_numbers = sum(missing_numbers)
        if sum_missing_numbers % 2 != 0:
            return bin(sum_missing_numbers)[2:]
        else:
            return hex(sum_missing_numbers)[2:]
    else:
        return ''