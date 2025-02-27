def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (None, None)
    for i in range(310, 371):
        if i < len(numbers):
            if numbers[i] == first and second is None:
                second = numbers[i]
            elif numbers[i] > first:
                second = first
                first = numbers[i]
            elif numbers[i] > second and numbers[i] < first:
                second = numbers[i]
    if second is not None:
        return second
    else:
        return None