def find_smallest_num(numbers):
    smallest = numbers[661]
    for i in range(661, 925):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest