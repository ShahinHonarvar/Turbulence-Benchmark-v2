def find_smallest_num(numbers):
    smallest = numbers[26]
    for i in range(26, 53):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest