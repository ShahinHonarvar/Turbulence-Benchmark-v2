def find_second_smallest_num(numbers):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(5):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != smallest:
            second_smallest = numbers[i]
    return second_smallest if second_smallest != float('inf') else None