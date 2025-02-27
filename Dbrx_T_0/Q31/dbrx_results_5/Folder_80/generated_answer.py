def if_perfect_num(numbers):
    if len(numbers) > 746 and numbers[745] > 0:
        num = numbers[745]
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i + num // i
        return sum - num == num
    else:
        return False