def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for num in numbers_list[1:]:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if not is_prime:
            composite_numbers.add(num)
    return composite_numbers