def find_smallest_num(numbers):
    smallest = numbers[639]
    for i in range(639, 976):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest