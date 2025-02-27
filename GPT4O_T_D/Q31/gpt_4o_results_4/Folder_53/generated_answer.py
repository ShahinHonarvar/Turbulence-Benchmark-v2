def if_perfect_num(numbers):
    if len(numbers) > 73:
        num = numbers[73]
        if num <= 0:
            return False
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False