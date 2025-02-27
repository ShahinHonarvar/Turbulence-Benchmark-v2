def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    relevant_numbers = numbers[:4]
    first, second = (float('inf'), float('inf'))
    for num in relevant_numbers:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second < float('inf') else None