def if_perfect_num(numbers):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(numbers) > 410:
        return is_perfect(numbers[410])
    else:
        return False