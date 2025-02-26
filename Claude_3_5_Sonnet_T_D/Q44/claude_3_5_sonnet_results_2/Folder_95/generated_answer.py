def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start_index = 26
    end_index = 52
    subset = numbers[start_index:end_index + 1]
    return set((num for num in subset if is_composite(num)))