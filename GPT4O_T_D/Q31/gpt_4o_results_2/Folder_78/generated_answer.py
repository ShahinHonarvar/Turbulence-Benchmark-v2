def if_perfect_num(numbers):

    def is_perfect(num):
        if num < 2:
            return False
        return sum((i for i in range(1, num) if num % i == 0)) == num
    if len(numbers) > 91:
        return is_perfect(numbers[91])
    return False