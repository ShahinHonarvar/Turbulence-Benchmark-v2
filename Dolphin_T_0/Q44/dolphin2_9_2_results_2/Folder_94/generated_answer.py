def composite_nums_between_indices(nums_list):

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(nums_list) if i >= 27 and i <= 55 and (num > 1) and all((num % i for i in range(2, int(num ** 0.5) + 1)))))