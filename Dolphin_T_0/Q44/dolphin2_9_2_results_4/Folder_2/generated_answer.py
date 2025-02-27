def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for x in range(2, n):
            if n % x == 0:
                return True
        return False
    composite_set = set()
    for num in numbers[35:50]:
        if is_composite(num):
            composite_set.add(num)
    return composite_set