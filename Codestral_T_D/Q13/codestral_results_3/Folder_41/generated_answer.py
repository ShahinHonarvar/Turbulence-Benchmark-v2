def find_second_largest_num(numbers):
    if len(numbers[6:8]) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in numbers[6:8]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if second != float('-inf') else None