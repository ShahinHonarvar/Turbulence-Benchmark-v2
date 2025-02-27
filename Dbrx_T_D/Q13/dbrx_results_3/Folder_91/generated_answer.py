def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers[:6])
    second_largest = float('-inf')
    for num in numbers[:6]:
        if first_largest > num > second_largest:
            second_largest = num
    if second_largest != first_largest and second_largest != float('-inf'):
        return second_largest
    else:
        return None