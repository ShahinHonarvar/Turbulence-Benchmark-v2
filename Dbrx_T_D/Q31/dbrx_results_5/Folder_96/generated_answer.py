def if_perfect_num(numbers):
    if len(numbers) < 47:
        return False
    target_number = numbers[46]
    divisor_sum = sum([i for i in range(1, target_number) if target_number % i == 0])
    return divisor_sum == target_number