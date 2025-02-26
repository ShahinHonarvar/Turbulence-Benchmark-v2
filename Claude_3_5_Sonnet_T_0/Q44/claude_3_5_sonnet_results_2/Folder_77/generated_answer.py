def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 667
    end_index = 774
    composite_set = set()
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set