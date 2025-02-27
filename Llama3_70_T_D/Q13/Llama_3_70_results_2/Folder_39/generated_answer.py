def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    else:
        second_largest = sorted(numbers[20:31])[-2]
        return second_largest