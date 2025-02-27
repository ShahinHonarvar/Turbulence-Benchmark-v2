def composite_nums_between_indices(lst):

    def is_composite(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return True
        return False
    return set((num for num in lst[30:88] if is_composite(num)))