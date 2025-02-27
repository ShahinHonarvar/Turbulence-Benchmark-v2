def if_perfect_num(numbers):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    return is_perfect(numbers[27]) if len(numbers) > 27 else False