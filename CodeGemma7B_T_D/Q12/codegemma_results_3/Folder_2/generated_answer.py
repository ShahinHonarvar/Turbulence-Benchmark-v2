def find_smallest_num(numbers):
    smallest_num = float('inf')
    for num in numbers[40:81]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num