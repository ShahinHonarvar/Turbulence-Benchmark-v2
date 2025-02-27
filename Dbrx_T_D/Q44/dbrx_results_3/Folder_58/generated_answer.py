def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(533, 606):
        num = numbers[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            composite_set.add(num)
    return composite_set