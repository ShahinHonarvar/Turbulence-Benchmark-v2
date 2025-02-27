def if_perfect_num(numbers):
    if 42 >= len(numbers):
        return False
    num = numbers[42]
    return sum((i for i in range(1, num) if num % i == 0)) == num