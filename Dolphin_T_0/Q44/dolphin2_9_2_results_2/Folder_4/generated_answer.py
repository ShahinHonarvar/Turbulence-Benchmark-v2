def composite_nums_between_indices(data):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for i in range(56, 99):
        if is_composite(data[i]):
            composite_nums.add(data[i])
    return composite_nums