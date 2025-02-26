def find_largest_num(numbers):
    if len(numbers) <= 10:
        return None
    end_index = min(101, len(numbers))
    return max(numbers[10:end_index])