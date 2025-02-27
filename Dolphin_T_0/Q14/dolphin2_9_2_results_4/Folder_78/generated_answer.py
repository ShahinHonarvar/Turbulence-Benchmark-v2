def find_second_smallest_num(numbers):
    numbers = numbers[16:79]
    if len(numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num > smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None