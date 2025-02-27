def if_perfect_num(numbers):
    number = numbers[851]
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        return True
    else:
        return False