def find_smallest_num(numbers):
    if len(numbers) == 0:
        return None
    smallest_num = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest_num:
            smallest_num = numbers[i]
    return smallest_num