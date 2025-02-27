def if_perfect_num(numbers):

    def sum_divisors(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors)
    return sum_divisors(numbers[478]) == numbers[478]