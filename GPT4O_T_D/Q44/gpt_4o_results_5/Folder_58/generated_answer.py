def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num <= 1:
            return False
        if num == 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_set = set()
    if len(numbers) > 605:
        for num in numbers[533:606]:
            if is_composite(num):
                composite_set.add(num)
    return composite_set