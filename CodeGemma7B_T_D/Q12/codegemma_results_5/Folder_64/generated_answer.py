def find_smallest_num(numbers):
    smallest = numbers[0]
    for num in numbers[0:4]:
        if num < smallest:
            smallest = num
    return smallest