def if_perfect_num(numbers):
    if len(numbers) > 746 and numbers[745] > 0:
        num = numbers[745]
        divisor_sum = sum([i for i in range(1, num) if num % i == 0])
        return divisor_sum == num
    else:
        return False