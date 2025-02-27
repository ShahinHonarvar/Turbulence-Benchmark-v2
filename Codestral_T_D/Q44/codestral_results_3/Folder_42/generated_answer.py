def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(91, 100):
        num = numbers[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_set.add(num)
                    break
    return composite_set