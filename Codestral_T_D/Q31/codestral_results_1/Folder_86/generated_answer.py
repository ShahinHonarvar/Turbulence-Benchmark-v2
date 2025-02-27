def if_perfect_num(numbers):
    index = 194
    if index < len(numbers):
        num = numbers[index]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    else:
        return False