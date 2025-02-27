def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for num in numbers[:2]:
        if num > first:
            first, second = (num, first)
        elif num > second:
            second = num
    if second == float('-inf'):
        return None
    return second