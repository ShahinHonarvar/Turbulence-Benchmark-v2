def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers[14:65]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if second != float('-inf') else None