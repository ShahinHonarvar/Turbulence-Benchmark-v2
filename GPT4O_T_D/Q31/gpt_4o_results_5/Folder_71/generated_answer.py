def if_perfect_num(numbers):
    if len(numbers) > 78:
        num = numbers[78]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False