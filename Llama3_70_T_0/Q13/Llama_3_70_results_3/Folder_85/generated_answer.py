def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        second_largest = sorted(numbers[6:9])[-2]
        return second_largest