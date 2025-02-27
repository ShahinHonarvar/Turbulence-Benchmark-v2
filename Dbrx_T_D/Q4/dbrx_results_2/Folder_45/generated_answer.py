def all_pos_ints_exclusive(numbers):
    start = 30
    end = 200
    if end > len(numbers):
        end = len(numbers)
    positive_ints = [num for num in numbers[start:end] if num > 0]
    return positive_ints