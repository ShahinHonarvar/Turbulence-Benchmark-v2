def composite_nums_between_indices(input_list):

    def is_composite(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return True
        return False
    return set((num for num in input_list[667:775] if is_composite(num)))