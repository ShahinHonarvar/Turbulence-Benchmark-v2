def if_perfect_num(numbers):
    if len(numbers) > 64:
        target_number = numbers[63]
        sum_factor = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum_factor += i
        return sum_factor == target_number
    else:
        return False