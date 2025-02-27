def if_perfect_num(numbers):
    if len(numbers) > 95:
        target_number = numbers[95]
        sum_of_factors = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum_of_factors += i
        if sum_of_factors == target_number:
            return True
        else:
            return False
    else:
        return False