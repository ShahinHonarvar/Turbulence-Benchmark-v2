def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(43, 52):
        n = numbers[i]
        if n > 1 and (not (n & 1 and n % 3 == 0)) and all((n % d for d in range(2, int(n ** 0.5) + 1))):
            composite_set.add(n)
    return composite_set