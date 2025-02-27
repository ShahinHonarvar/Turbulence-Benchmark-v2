def if_perfect_num(numbers):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(numbers) > 53:
        return is_perfect(numbers[53])
    else:
        return False