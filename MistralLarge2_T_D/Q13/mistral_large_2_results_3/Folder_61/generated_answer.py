def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for num in numbers[:8]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None