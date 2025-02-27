def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    for i in range(64, 67):
        if i < len(num_list) and is_composite(num_list[i]):
            result.add(num_list[i])
    return result