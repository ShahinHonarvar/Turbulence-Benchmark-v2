def find_second_smallest_num(numbers):
    if len(numbers) < 64 or len(numbers[62:64]) < 2:
        return None
    sublist = numbers[62:64]
    smallest = min(sublist)
    second_smallest = min((num for num in sublist if num != smallest))
    return second_smallest