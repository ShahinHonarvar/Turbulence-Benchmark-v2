def if_perfect_num(numbers):
    num = numbers[74]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i == num / i:
                sum = sum + i
            else:
                sum = sum + (i + num // i)
    if sum == num:
        return True
    else:
        return False