def if_perfect_num(numbers):
    num = numbers[94]
    total = 1
    for i in range(2, num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False