def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    first_smallest, second_smallest = (min(numbers[0:8]), float('inf'))
    for num in numbers[0:8]:
        if first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest < float('inf') else None