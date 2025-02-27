def find_smallest_num(numbers):
    smallest = numbers[13]
    for i in range(13, 69):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest