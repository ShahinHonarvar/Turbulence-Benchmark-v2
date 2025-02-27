def composite_nums_between_indices(arr):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            else:
                return False
    return {x for x in arr[314:348] if is_composite(x)}