def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        first_min = min(numbers[:10])
        second_min = float('inf')
        for i in range(10):
            if numbers[i] != first_min and numbers[i] < second_min:
                second_min = numbers[i]
        if second_min == float('inf'):
            return None
        else:
            return second_min