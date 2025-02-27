def all_neg_ints_exclusive(numbers):
    return [numbers[i] for i in range(len(numbers)) if 8 <= i <= 9 and numbers[i] < 0]