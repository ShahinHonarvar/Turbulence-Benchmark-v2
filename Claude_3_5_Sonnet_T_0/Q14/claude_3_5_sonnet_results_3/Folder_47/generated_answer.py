def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[22:64]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None