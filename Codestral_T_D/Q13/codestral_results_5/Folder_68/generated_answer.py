def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:9]) < 2:
        return None
    first = second = float('-inf')
    for num in numbers[:9]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None