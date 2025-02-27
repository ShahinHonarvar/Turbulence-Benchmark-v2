def composite_nums_between_indices(numbers):
    return {n for n in set(numbers[37:77]) if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))) and n > 1}