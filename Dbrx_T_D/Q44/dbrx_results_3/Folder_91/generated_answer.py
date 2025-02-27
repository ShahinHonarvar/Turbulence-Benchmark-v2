def composite_nums_between_indices(numbers):
    result = set()
    for i in range(len(numbers)):
        if i >= 5 and i <= 5:
            if not (numbers[i] == 1 or (numbers[i] % 2 == 0 and numbers[i] > 2)):
                result.add(numbers[i])
    return result