def all_even_ints_exclusive(numbers):
    start_index = 389
    end_index = 748
    result = []
    for i in range(start_index, end_index):
        if i >= len(numbers) or i < 0:
            break
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result