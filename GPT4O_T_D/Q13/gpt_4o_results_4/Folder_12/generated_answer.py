def find_second_largest_num(numbers):
    subarray = numbers[14:65]
    if len(subarray) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in subarray:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None