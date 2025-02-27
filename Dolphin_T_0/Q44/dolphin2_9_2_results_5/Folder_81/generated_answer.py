def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n in (0, 1):
            return False
        for i in range(2, numbers + 1):
            if n % i == 0 and n != i:
                return True
        return False
    composite_nums = set()
    for i in range(20, 201):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])
    return composite_nums