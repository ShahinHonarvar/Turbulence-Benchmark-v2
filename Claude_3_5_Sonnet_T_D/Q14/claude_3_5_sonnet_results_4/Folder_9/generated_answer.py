def find_second_smallest_num(numbers):
    if len(numbers) < 71:
        return None
    start = 70
    end = min(200, len(numbers) - 1)
    sublist = numbers[start:end + 1]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None