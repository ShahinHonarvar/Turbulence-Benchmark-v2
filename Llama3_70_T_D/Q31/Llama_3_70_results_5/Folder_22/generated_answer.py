def if_perfect_num(numbers):

    def sum_of_divisors(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    if len(numbers) > 72:
        return sum_of_divisors(numbers[72]) == numbers[72]
    else:
        return False