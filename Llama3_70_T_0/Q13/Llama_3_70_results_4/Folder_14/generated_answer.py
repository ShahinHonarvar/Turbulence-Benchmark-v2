def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    else:
        second_largest = sorted(numbers[5:8])[1]
        return second_largest