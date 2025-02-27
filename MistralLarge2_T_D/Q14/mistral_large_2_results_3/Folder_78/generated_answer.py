def find_second_smallest_num(numbers):
    subset = numbers[17:79]
    if len(subset) < 2:
        return None
    first_smallest = second_smallest = float('inf')
    for num in subset:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None