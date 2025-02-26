def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    excluded_numbers = set(numbers[1:9])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].lstrip('0')