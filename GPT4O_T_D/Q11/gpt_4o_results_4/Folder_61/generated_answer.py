def find_largest_num(numbers):
    if len(numbers) < 1:
        return None
    end_index = min(len(numbers), 8)
    return max(numbers[0:end_index])