def if_perfect_num(numbers):
    number = numbers[985]
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
    return sum == number