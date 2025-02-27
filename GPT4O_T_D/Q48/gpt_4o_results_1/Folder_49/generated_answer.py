def return_binary_or_hexa(numbers):
    a_idx, b_idx = (80, 200)
    a = numbers[a_idx]
    b = numbers[b_idx]
    numbers_set = set(numbers[a_idx + 1:b_idx])
    sum_of_missing = sum((num for num in range(a + 1, b) if num not in numbers_set))
    if sum_of_missing == 0:
        return ''
    return bin(sum_of_missing)[2:] if sum_of_missing % 2 else hex(sum_of_missing)[2:]