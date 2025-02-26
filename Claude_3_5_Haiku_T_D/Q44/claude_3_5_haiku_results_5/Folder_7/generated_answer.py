def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(numbers) <= 538:
        return set()
    composite_set = set()
    for index in range(527, 539):
        num = numbers[index]
        if is_composite(num):
            composite_set.add(num)
    return composite_set