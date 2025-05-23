def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = set()
    for index in range(25, min(len(lst), 60)):
        if is_composite(lst[index]):
            composites.add(lst[index])
    return composites