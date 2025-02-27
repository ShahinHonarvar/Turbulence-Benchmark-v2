def is_perfect(num):
    return num == sum((i for i in range(1, num) if num % i == 0))

def if_perfect_num(numbers):
    return is_perfect(numbers[67]) if len(numbers) > 67 else False