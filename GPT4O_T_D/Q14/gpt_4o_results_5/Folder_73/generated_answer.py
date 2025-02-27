def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers[59:98]) < 2:
        return None
    sublist = numbers[59:98]
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None