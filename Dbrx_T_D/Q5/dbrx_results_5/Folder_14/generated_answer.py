def all_neg_ints_inclusive(numbers):
    start = 4
    end = 6
    return [num for num in numbers[start:end + 1] if num < 0]