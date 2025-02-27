def composite_nums_between_indices(positive_integers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    result = set()
    for i in range(17, 79):
        if is_composite(positive_integers[i]):
            result.add(positive_integers[i])
    return result