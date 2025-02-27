def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[49:75]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing == 0:
        return ''
    else:
        return hex(sum_missing)[2:]