def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    relevant_numbers = numbers[10:101]
    if len(relevant_numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in relevant_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None