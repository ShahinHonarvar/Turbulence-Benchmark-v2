def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 60 or len(numbers) < 200:
        return None
    min_num_1 = float('inf')
    min_num_2 = float('inf')
    for num in numbers[60:201]:
        if num < min_num_1:
            min_num_2 = min_num_1
            min_num_1 = num
        elif num < min_num_2 and num > min_num_1:
            min_num_2 = num
    if min_num_2 == float('inf'):
        return None
    else:
        return min_num_2