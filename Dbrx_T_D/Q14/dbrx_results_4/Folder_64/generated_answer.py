def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:5]) < 2:
        return None
    first_smallest_index = numbers.index(min(numbers[:5]))
    second_smallest = float('inf')
    second_smallest_index = -1
    for i in range(len(numbers)):
        if i == first_smallest_index:
            continue
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
            second_smallest_index = i
    if second_smallest_index == -1:
        return None
    else:
        return second_smallest