def all_neg_ints_exclusive(numbers):
    start_index = 389
    end_index = 748
    if len(numbers) <= end_index:
        return []
    return [num for num in numbers[start_index:end_index] if num < 0]