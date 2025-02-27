def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    selected_numbers = numbers[17:79]
    if len(selected_numbers) < 2:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in selected_numbers:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None