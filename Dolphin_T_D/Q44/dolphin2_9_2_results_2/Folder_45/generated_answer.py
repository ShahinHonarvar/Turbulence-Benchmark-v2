def composite_nums_between_indices(numbers):

    def is_composite(num):
        if num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    result = [i for i in numbers[40:200] if is_composite(i)]
    return set(result)