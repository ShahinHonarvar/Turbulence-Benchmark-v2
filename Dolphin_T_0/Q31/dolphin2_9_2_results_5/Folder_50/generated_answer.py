def if_perfect_num(numbers):

    def is_perfect(num):
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(numbers) > 40:
        return is_perfect(numbers[40])
    else:
        return False