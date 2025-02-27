def if_perfect_num(numbers):

    def is_perfect_number(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n
    return is_perfect_number(numbers[96])