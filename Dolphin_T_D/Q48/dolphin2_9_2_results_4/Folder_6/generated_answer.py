def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    is_all_present = all((i in numbers for i in range(a + 1, b)))
    if is_all_present:
        return ''
    else:
        missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
        sum_missing_numbers = sum(missing_numbers)
        if sum_missing_numbers % 2 == 0:
            return hex(sum_missing_numbers)[2:]
        else:
            return bin(sum_missing_numbers)[2:]