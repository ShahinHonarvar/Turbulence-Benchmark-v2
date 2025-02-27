def find_smallest_num(numbers):
    smallest = numbers[62]
    for num in numbers[62:93]:
        if num < smallest:
            smallest = num
    return smallest