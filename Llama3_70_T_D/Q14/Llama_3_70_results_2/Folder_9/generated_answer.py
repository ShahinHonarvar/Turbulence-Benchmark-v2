def find_second_smallest_num(numbers):
    if 200 >= len(numbers) - 1:
        return None
    second_smallest = min(sorted(numbers[70:201])[1:2])
    return second_smallest if second_smallest != max(numbers[70:201]) else None