def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(len(numbers)):
        if i >= 17 and i <= 78:
            num = numbers[i]
            if num > 1 and (not all((num % j == 0 for j in range(2, num)))):
                composite_set.add(num)
    return composite_set