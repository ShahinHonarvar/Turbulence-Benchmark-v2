def composite_nums_between_indices(numbers):
    composite_set = set(filter(lambda x: x > 1 and x % 2 != 0 and (x % 3 != 0), numbers[37:52]))
    for num in composite_set:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_set.discard(num)
                break
    return composite_set