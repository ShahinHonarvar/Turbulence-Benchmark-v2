def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    sublist = numbers[31:73]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None