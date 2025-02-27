def composite_nums_between_indices(nums_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {num for num in nums_list[43:52] if is_composite(num)}