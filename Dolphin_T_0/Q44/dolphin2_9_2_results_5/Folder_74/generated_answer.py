def composite_nums_between_indices(numbers):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    comp_nums = set()
    for i in range(42, 69):
        if is_composite(numbers[i]):
            comp_nums.add(numbers[i])
    return comp_nums