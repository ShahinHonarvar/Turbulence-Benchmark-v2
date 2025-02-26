def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for index in range(min(6, len(numbers))):
        if is_composite(numbers[index]):
            composite_set.add(numbers[index])
    return composite_set