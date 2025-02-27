def find_smallest_num(numbers):
    smallest = float('inf')
    for number in numbers[20:201]:
        if number < smallest:
            smallest = number
    return smallest