def if_perfect_num(numbers):
    if len(numbers) <= 90:
        return False
    num = numbers[90]
    if num < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum == num