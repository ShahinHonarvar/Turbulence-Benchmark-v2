def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(22, 89):
        num = numbers[i]
        if num > 1 and (not all((num % j for j in range(2, num)))):
            composite_set.add(num)
    return composite_set