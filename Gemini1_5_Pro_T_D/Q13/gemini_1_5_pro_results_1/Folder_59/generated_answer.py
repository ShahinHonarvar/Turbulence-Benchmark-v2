def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    largest = max(numbers[0:10])
    second_largest = min(numbers[0:10])
    for i in range(len(numbers)):
        if i < 10:
            if numbers[i] != largest and numbers[i] > second_largest:
                second_largest = numbers[i]
    if second_largest == largest:
        return None
    else:
        return second_largest