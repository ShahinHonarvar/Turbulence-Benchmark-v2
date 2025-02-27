def find_smallest_num(numbers):
    return min(numbers[0:numbers.index(min(numbers)) + 1])