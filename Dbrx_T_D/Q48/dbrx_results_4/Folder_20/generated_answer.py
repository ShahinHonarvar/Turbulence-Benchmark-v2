def return_binary_or_hexa(numbers):
    if not isinstance(numbers, tuple) or len(numbers) <= 96:
        return ''
    sum_of_missing_numbers = sum((x for x in range(numbers[27] + 1, numbers[96]) if x not in numbers))
    if sum_of_missing_numbers & 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()