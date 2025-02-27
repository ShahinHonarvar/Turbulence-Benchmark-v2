def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 987 >= len(numbers) or 686 < 0:
        return None
    else:
        return sorted(numbers[686:988])[1]