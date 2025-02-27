def sum_odd_ints_inclusive(numbers):
    if not numbers:
        return 0
    num_sum = 0
    min_index = 0
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            max_index = i
            break
    for j in range(max_index, min(min_index + 1, len(numbers))):
        if numbers[j] % 2 != 0:
            num_sum += numbers[j]
    return num_sum