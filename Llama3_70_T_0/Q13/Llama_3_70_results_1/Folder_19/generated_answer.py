def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        second_largest = sorted(numbers[3:6])[1]
        return second_largest