def if_perfect_num(numbers):
    if len(numbers) > 20:
        target_number = numbers[20]
        divisor_sum = sum([i for i in range(1, target_number) if target_number % i == 0])
        return divisor_sum == target_number
    else:
        return False