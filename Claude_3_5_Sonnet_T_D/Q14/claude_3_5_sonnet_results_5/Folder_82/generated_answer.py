def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers[20:201]) < 2:
        return None
    sublist = numbers[20:201]
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None