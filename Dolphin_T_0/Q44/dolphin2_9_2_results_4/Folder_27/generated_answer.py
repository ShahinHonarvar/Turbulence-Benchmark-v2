def composite_nums_between_indices(numbers):
    result = set()
    for i in range(22, 64):
        if numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    result.add(numbers[i])
                    break
    return result