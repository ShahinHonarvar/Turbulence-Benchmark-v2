def if_perfect_num(numbers):

    def is_perfect(number):
        if number < 2:
            return False
        sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
        return sum_of_divisors == number
    if not numbers:
        return False
    return is_perfect(numbers[0])