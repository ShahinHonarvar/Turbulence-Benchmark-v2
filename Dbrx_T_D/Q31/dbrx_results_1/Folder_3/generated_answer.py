def if_perfect_num(numbers):
    if len(numbers) > 100:
        target_number = numbers[100]
        sum_of_factors = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum_of_factors += i
        return sum_of_factors == target_number
    else:
        return False