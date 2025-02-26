def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start = min(30, len(numbers))
    end = min(30, len(numbers))
    return set((num for num in numbers[start:end + 1] if is_composite(num)))