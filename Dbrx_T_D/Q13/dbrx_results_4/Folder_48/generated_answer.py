def find_second_largest_num(numbers):
    try:
        second_largest = max(numbers[533:606])
        second_largest_index = numbers.index(second_largest, 533, 606)
        if second_largest == max(numbers[533:606]):
            second_largest = numbers[second_largest_index - 1]
            second_largest_index = numbers.index(second_largest, 533, 606)
    except ValueError:
        return None
    else:
        return second_largest