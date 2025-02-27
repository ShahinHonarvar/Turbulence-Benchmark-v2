def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    return False
                i += 1
        return True
    return set((num for i, num in enumerate(num_list[1:6], 1) if is_composite(num)))