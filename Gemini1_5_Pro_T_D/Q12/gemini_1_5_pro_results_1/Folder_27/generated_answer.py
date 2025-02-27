def find_smallest_num(numbers):
    smallest = numbers[62]
    for i in range(62, 93):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest