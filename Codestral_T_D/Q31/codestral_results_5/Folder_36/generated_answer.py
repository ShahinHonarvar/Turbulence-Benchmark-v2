def if_perfect_num(numbers):

    def is_perfect_number(n):
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == n
    return is_perfect_number(numbers[990])