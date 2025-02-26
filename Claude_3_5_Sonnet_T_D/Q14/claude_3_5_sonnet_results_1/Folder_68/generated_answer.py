def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 8:
        return None
    relevant_numbers = numbers[:9]
    smallest = min(relevant_numbers)
    second_smallest = float('inf')
    for num in relevant_numbers:
        if num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None