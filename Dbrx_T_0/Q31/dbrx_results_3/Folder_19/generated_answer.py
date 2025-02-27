def if_perfect_num(numbers):
    if len(numbers) > 13 and numbers[13] > 0:
        num = numbers[13]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    else:
        return False