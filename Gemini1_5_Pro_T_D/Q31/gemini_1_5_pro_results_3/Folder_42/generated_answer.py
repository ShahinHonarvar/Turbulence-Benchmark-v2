def if_perfect_num(numbers):
    if len(numbers) <= 276:
        return False
    number = numbers[276]
    if number <= 1:
        return False
    sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum += i + number // i
    return sum == number