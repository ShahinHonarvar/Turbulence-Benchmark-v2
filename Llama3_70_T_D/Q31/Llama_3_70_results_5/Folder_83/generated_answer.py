def if_perfect_num(numbers):

    def is_perfect(num):
        divisors = [n for n in range(1, num) if num % n == 0]
        return sum(divisors) == num
    return is_perfect(numbers[95])