def if_perfect_num(numbers):
    if len(numbers) <= 849:
        return False
    num = numbers[849]
    if num <= 1:
        return False
    divisor_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
    return divisor_sum == num