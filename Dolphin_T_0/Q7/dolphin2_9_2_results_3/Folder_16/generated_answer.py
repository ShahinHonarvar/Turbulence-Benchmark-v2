def all_even_ints_inclusive(numbers, start_idx=33, end_idx=36):
    return [num for num in numbers[start_idx:end_idx + 1] if num % 2 == 0]