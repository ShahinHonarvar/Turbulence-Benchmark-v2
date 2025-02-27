def find_second_largest_num(numbers):
    sublist = numbers[59:98]
    if len(sublist) < 2:
        return None
    first = second = float('-inf')
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None