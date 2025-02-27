def if_perfect_num(numbers):

    def is_perfect(num):
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return is_perfect(numbers[68]) if len(numbers) > 68 else False