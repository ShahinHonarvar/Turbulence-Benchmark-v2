def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 639
    end_index = 975
    composite_set = set()
    for index in range(max(0, start_index), min(len(numbers), end_index + 1)):
        if is_composite(numbers[index]):
            composite_set.add(numbers[index])
    return composite_set