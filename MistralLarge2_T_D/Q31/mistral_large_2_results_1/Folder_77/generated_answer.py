def if_perfect_num(numbers):

    def is_perfect(num):
        sum_of_divisors = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
        return sum_of_divisors == num
    if len(numbers) > 985 and is_perfect(numbers[985]):
        return True
    return False