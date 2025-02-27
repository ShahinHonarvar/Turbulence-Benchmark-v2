def find_smallest_num(numbers):
    smallest_num = float('inf')
    for i in range(len(numbers)):
        if numbers[i] < smallest_num and i <= 2:
            smallest_num = numbers[i]
    return smallest_num