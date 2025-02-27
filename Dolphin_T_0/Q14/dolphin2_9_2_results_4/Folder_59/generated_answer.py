def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        smallest = float('inf')
        second_smallest = float('inf')
        for i in numbers[0:10]:
            if i < smallest:
                second_smallest = smallest
                smallest = i
            elif i < second_smallest and i != smallest:
                second_smallest = i
        if second_smallest == float('inf'):
            return None
        else:
            return second_smallest