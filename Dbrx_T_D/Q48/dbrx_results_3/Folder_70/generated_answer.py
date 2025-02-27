def return_binary_or_hexa(numbers):
    if not isinstance(numbers, tuple) or len(numbers) < 71 or any((not isinstance(i, int) or i < 0 for i in numbers)):
        raise ValueError('Input must be a tuple of distinct nonnegative integers sorted in ascending order with length at least 71.')
    a, b = (numbers[43], numbers[70])
    if a >= b:
        raise ValueError('The value at index 43 must be less than the value at index 70.')
    missing_numbers = set(range(a + 1, b))
    for num in numbers[44:70]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()