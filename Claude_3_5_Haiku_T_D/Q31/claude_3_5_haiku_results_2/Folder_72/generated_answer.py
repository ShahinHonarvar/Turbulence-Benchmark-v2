def if_perfect_num(numbers):

    def is_perfect(num):
        if num <= 0:
            return False
        divisor_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisor_sum == num
    if len(numbers) <= 16:
        return False
    return is_perfect(numbers[16])