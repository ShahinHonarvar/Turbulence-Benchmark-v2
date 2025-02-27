def composite_nums_between_indices(numbers):

    def is_composite(number):
        if number <= 1:
            return False
        if number <= 3:
            return False
        if number % 2 == 0 or number % 3 == 0:
            return True
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for num in numbers[50:55] if is_composite(num)}