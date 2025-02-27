def if_perfect_num(numbers):
    num = numbers[17]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * (num / i) == num:
                sum += i
            else:
                sum += i + num / i
        i += 1
    return sum == num and num != 1