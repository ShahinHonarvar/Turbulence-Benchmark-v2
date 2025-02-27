def if_perfect_num(numbers):

    def is_perfect(num):
        if num <= 1:
            return False
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    if len(numbers) > 57:
        return is_perfect(numbers[57])
    return False