def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    non_present_numbers = set(range(a + 1, b)) - set(numbers[43:71])
    if not non_present_numbers:
        return ''
    sum_of_non_present = sum(non_present_numbers)
    if sum_of_non_present % 2:
        return bin(sum_of_non_present)[2:]
    else:
        return hex(sum_of_non_present)[2:].upper()