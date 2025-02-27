def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers[:10]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None