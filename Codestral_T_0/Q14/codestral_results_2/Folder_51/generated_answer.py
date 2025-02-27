def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[1:9]
    if len(sublist) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest