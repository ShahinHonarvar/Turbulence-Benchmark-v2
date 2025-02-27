def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        first = second = float('inf')
        for i in range(10):
            if numbers[i] < first:
                second = first
                first = numbers[i]
            elif numbers[i] < second and numbers[i] != first:
                second = numbers[i]
        if second == float('inf'):
            return None
        else:
            return second