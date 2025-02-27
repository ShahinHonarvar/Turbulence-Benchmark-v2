def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    min_two = [None, None]
    for num in numbers[26:53]:
        if min_two[0] is None or num < min_two[0]:
            min_two[1] = min_two[0]
            min_two[0] = num
        elif min_two[1] is None or num < min_two[1]:
            min_two[1] = num
    return min_two[1] if min_two[0] is not None else None