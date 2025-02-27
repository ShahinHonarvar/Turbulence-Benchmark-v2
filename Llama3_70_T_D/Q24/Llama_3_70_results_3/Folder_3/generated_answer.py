def sum_of_divisors_in_range(n):

    def get_divisors(num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    divisors = get_divisors(n)
    sum_divisors = sum([divisor for divisor in divisors if 43 <= divisor <= 46])
    return sum_divisors