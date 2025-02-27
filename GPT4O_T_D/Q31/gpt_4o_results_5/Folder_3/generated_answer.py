def if_perfect_num(numbers):

    def is_perfect(number):
        if number < 2:
            return False
        sum_divisors = 1
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                sum_divisors += i
                if i != number // i:
                    sum_divisors += number // i
        return sum_divisors == number
    if len(numbers) > 100:
        return is_perfect(numbers[100])
    return False