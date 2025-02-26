def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(numbers) < 64:
        return set()
    composite_set = set()
    for i in range(22, 64):
        if is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set