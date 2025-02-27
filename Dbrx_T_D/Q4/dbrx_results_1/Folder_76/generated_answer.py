def all_pos_ints_exclusive(numbers):
    highlighted_numbers = numbers[360:642]
    positive_numbers = [num for num in highlighted_numbers if num > 0]
    return positive_numbers