def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for idx in range(36, 47):
        if idx < len(numbers):
            num = numbers[idx]
            if is_composite(num):
                composite_set.add(num)
    return composite_set