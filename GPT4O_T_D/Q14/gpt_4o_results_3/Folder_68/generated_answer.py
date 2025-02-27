def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    first = float('inf')
    second = float('inf')
    for num in numbers[:9]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second < float('inf') else None