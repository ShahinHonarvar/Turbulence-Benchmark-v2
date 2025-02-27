def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num <= 1:
            return False
        if num in (2, 3):
            return False
        if num % 2 == 0 or num % 3 == 0:
            return True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for num in numbers[64:67] if is_composite(num)}