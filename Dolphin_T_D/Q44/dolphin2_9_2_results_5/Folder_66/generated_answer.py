def composite_nums_between_indices(numbers):

    def is_composite_number(n):
        if n == 1:
            return False
        for num in range(2, int(n ** 0.5) + 1):
            if n % num == 0:
                return True
        return False
    return {num for num in numbers[62:64] if is_composite_number(num)}