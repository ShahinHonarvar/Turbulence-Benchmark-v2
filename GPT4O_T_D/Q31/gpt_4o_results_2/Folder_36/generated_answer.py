def if_perfect_num(numbers):

    def is_perfect_number(n):
        if n < 2:
            return False
        divisors_sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum == n
    if len(numbers) <= 990:
        return False
    return is_perfect_number(numbers[990])