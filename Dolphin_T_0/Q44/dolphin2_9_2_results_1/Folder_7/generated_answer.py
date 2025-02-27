def composite_nums_between_indices(nums_list):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {nums_list[i] for i in range(527, 539) if is_composite(nums_list[i])}