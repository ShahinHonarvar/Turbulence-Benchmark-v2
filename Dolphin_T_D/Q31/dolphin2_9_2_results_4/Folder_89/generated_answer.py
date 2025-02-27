def if_perfect_num(numbers):
    if len(numbers) < 19:
        return False
    num = numbers[18]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i == num / i:
                sum += i
            else:
                sum += i + num / i
            i += 1
    return sum == num and num != 1