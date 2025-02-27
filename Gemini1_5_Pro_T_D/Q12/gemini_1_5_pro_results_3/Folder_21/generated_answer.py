def find_smallest_num(numbers):
    smallest = numbers[686]
    for i in range(687, 988):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest