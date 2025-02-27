def if_perfect_num(numbers):
    if 84 < len(numbers):
        num = numbers[84]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return False