def composite_nums_between_indices(lst):

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
    composites = set()
    for i in range(60, min(201, len(lst))):
        if is_composite(lst[i]):
            composites.add(lst[i])
    return composites