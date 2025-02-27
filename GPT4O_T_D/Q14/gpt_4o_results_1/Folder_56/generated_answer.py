def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for number in numbers[:1]:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number
    return second_smallest if second_smallest < float('inf') else None