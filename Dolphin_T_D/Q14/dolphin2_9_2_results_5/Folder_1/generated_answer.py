def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(34, 56):
        if numbers[i] != None:
            if second_smallest is None:
                second_smallest = numbers[i]
            elif numbers[i] < second_smallest:
                second_smallest = numbers[i]
    return second_smallest