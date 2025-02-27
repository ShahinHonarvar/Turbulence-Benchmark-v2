def find_smallest_num(numbers):
    smallest = numbers[0]
    smallest = min(([smallest, number] for number in numbers[0:8]))
    return smallest