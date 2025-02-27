def sum_even_ints_inclusive(numbers):
    if len(numbers) < 774:
        return 'Input list is too short.'
    elif len(numbers) >= 775:
        return 'Input list is too long.'
    else:
        sum = 0
        for i in range(667, 775):
            if numbers[i] % 2 == 0:
                sum += numbers[i]
        return sum