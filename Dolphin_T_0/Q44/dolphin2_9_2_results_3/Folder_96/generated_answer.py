def composite_nums_between_indices(arr):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return {num for num in arr[60:201] if is_composite(num)}