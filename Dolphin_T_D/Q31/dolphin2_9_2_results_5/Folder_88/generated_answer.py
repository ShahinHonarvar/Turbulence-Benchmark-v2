def if_perfect_num(numbers):
    num = numbers[46]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * (num // i) == num:
                sum = sum + i + num // i
            else:
                sum = sum + i
        i = i + 1
    return sum == num