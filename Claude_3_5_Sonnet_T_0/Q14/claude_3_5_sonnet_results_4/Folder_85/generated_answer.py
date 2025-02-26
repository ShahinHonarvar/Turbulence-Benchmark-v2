def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:7]) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers[:7]:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None