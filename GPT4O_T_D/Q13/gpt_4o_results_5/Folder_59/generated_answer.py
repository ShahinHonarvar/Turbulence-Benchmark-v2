def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[:10]
    if len(sublist) < 2:
        return None
    first = second = float('-inf')
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None