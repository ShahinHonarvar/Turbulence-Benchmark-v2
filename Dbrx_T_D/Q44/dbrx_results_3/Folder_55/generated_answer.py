def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 10 and i <= 100:
            num = numbers[i]
            if num > 1 and (not all((num % j == 0 for j in range(2, num)))):
                composite_numbers.add(num)
    return composite_numbers