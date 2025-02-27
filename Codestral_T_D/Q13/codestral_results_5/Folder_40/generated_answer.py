def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers[:3]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return None if second == float('-inf') else second