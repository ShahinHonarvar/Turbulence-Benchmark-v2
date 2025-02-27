def if_perfect_num(numbers):

    def perfect_num(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(numbers) > 926 and numbers[926] > 0:
        return perfect_num(numbers[926])
    return False