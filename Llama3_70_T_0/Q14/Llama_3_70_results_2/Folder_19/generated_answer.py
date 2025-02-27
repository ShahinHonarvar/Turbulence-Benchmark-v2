def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        second_smallest = sorted(numbers[4:9])[1]
        return second_smallest