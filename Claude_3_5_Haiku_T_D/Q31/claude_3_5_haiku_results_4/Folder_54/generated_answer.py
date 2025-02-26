def if_perfect_num(numbers):

    def is_perfect(num):
        if num <= 0:
            return False
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    if len(numbers) <= 51:
        return False
    return is_perfect(numbers[51])