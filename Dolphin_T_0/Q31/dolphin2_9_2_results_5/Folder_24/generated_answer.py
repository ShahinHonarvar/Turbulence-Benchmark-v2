def if_perfect_num(numbers):
    if len(numbers) < 75:
        return False
    number = numbers[74]
    sum = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        elif i == number // i:
            sum = sum + i
            i += 1
        else:
            sum = sum + (i + number // i)
            i += 1
    return sum == number