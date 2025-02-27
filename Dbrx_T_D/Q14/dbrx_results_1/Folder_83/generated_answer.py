def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 90:
        return None
    min_num = min_num_2 = float('inf')
    for i in range(90, 201):
        if numbers[i] < min_num:
            min_num_2 = min_num
            min_num = numbers[i]
        elif min_num < numbers[i] < min_num_2:
            min_num_2 = numbers[i]
    return min_num_2 if min_num_2 != float('inf') else None