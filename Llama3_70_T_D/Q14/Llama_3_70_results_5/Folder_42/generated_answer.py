def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    second_smallest = sorted(numbers[21:98])[1]
    return second_smallest