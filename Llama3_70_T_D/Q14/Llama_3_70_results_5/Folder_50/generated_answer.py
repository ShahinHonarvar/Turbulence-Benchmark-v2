def find_second_smallest_num(numbers):
    if 42 < len(numbers) < 69:
        return None
    else:
        second_smallest = sorted(set(numbers[42:69]))[1]
        return second_smallest