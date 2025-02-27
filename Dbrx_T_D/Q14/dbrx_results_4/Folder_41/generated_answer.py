def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    min_num = min(numbers[4:])
    if min_num == max(min_num, numbers[4 - 1]):
        return None
    second_smallest = min(set(numbers[4:]) - {min_num})
    return second_smallest if second_smallest != min_num else None