def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(222, min(223, len(numbers))):
        num = numbers[i]
        if num > 1 and (not all((num % j for j in range(2, num)))):
            composite_numbers.add(num)
    return composite_numbers