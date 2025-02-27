def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    else:
        second_smallest = float('inf')
        smallest = float('inf')
        for num in numbers[20:31]:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
        if second_smallest == float('inf'):
            return None
        else:
            return second_smallest