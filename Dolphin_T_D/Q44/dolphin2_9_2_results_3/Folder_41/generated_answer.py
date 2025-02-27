def composite_nums_between_indices(lst):

    def check_composite(n):
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set((num for num in lst[0:3] if check_composite(num)))