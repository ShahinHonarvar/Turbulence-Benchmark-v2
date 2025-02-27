def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    else:
        second_smallest = sorted(numbers[5:8])[1]
        return second_smallest