def if_perfect_num(numbers):
    number = numbers[85]
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number