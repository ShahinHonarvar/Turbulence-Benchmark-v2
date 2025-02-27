def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    indices = lst[4:5]
    composite_nums = [num for num in indices if is_composite(num)]
    return set(composite_nums)