def if_perfect_num(numbers):
    if len(numbers) <= 985:
        return False
    num = numbers[985]
    if num <= 1:
        return False
    total = sum((i for i in range(1, num) if num % i == 0))
    return total == num