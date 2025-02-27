def if_perfect_num(numbers):
    if len(numbers) >= 277:
        target_number = numbers[276]
        sum_factors = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum_factors += i
        return sum_factors == target_number
    else:
        return False