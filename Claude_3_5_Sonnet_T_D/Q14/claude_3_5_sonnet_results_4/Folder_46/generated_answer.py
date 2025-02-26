def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    relevant_numbers = numbers[13:69]
    if len(relevant_numbers) < 2:
        return None
    smallest = min(relevant_numbers)
    second_smallest = float('inf')
    for num in relevant_numbers:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None