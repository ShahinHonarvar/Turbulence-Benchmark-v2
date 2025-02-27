def find_smallest_num(numbers):
    subset = numbers[30:49]
    smallest = subset[0]
    for number in subset:
        if number < smallest:
            smallest = number
    return smallest