def find_second_largest_num(numbers):
    if 8 <= len(numbers) < 10:
        second_largest = sorted(numbers)[-2]
        return second_largest
    else:
        return None