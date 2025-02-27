def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(686, 988):
        num = numbers[i]
        if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
            composite_set.add(num)
    return composite_set