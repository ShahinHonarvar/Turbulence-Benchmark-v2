def return_binary_or_hexa(numbers):
    a_idx, b_idx = (2, 7)
    if len(numbers) <= b_idx or len(numbers) <= a_idx:
        return ''
    a, b = (numbers[a_idx], numbers[b_idx])
    all_numbers = set(range(a + 1, b))
    tuple_numbers = set(numbers[a_idx + 1:b_idx])
    missing_numbers = all_numbers - tuple_numbers
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]