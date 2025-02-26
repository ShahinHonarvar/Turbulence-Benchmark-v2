def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:9]) < 2:
        return None
    sublist = numbers[1:9]
    if len(sublist) == 2:
        return max(sublist)
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None