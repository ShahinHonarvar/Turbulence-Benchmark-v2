def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_numbers = set()
    for i in range(28, min(39, len(numbers))):
        if is_composite(numbers[i]):
            composite_numbers.add(numbers[i])
    return composite_numbers