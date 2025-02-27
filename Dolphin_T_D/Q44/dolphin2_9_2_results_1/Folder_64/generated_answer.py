def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    result = set()
    for num in lst[:5]:
        if is_composite(num):
            result.add(num)
    return result