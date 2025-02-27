def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[:8]
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None