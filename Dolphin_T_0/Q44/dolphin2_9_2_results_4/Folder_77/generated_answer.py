def composite_nums_between_indices(lst):

    def check_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    composite_numbers = set()
    for i in range(667, 775):
        if check_composite(lst[i]):
            composite_numbers.add(lst[i])
    return composite_numbers