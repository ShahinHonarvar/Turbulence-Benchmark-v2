def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num <= 1:
            return False
        if num <= 3:
            return False
        if num % 2 == 0 or num % 3 == 0:
            return True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6
        return False
    composite_set = set()
    for i in range(min(len(numbers), 8)):
        if is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set