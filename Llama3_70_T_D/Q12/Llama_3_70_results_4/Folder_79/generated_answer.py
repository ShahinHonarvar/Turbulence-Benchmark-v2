def find_smallest_num(numbers):
    smallest = numbers[1]
    for num in numbers[2:6]:
        if num < smallest:
            smallest = num
    return smallest