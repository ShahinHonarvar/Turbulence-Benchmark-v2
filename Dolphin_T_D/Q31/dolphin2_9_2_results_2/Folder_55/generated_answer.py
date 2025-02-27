def if_perfect_num(numbers):

    def is_perfect(num):
        if num <= 0:
            return False
        else:
            sum_proper_divisors = 0
            for i in range(1, num):
                if num % i == 0:
                    sum_proper_divisors += i
            return sum_proper_divisors == num
    return is_perfect(numbers[21])