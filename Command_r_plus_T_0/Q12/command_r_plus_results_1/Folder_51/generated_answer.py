def find_smallest_num(numbers):
    smallest = numbers[6]
    for num in numbers[6:]:
        if num < smallest:
            smallest = num
    return smallest