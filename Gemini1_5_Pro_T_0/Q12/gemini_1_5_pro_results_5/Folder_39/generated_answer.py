def find_smallest_num(numbers):
    smallest = numbers[52]
    for i in range(52, 72):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest