def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    smallest = min(numbers[:4])
    second_smallest = min([num for num in numbers[:4] if num != smallest])
    return second_smallest if second_smallest != smallest else None