def if_perfect_num(numbers):
    index = 68
    num = numbers[index]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num