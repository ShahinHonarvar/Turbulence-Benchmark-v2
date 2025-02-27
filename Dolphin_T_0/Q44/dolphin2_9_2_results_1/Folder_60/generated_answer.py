def composite_nums_between_indices(lst):

    def is_composite(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
            else:
                return False
        else:
            return False
    output = set()
    for i in range(29, 52):
        if is_composite(lst[i]):
            output.add(lst[i])
    return output