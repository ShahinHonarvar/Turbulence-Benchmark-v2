def composite_nums_between_indices(lst):

    def check_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return {num for num in lst[50:201] if check_composite(num)}