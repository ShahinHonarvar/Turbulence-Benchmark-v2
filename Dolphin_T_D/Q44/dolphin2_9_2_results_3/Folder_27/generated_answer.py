def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    composites = set()
    for num in lst[22:64]:
        if is_composite(num):
            composites.add(num)
    return composites