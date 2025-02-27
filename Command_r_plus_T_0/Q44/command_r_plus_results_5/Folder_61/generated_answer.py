def composite_nums_between_indices(numbers_list):
    composite_set = set()
    for index, num in enumerate(numbers_list[:8]):
        if index in [0, 1]:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            composite_set.add(num)
    return composite_set