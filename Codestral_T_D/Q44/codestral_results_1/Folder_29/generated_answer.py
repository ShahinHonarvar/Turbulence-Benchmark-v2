def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(52, 72):
        if numbers[i] > 1:
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    composite_nums.add(numbers[i])
                    break
    return composite_nums