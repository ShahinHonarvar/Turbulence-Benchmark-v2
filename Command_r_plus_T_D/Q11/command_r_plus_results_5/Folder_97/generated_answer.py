def find_largest_num(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('Input list is empty.')
    if len(numbers) < 81:
        raise ValueError('Input list must have at least 81 elements.')
    largest_num = float('-inf')
    for i in range(40, 81):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num