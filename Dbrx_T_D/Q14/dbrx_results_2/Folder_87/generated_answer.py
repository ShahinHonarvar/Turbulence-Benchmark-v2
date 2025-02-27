def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 22 or len(numbers) > 89:
        return None
    min_num = min(numbers[21:89])
    second_min_num = min((x for x in numbers[21:89] if x > min_num))
    return second_min_num