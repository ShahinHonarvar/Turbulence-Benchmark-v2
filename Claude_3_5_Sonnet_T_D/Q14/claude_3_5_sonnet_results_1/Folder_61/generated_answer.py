def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:8]) < 2:
        return None
    sublist = numbers[:8]
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None