def if_perfect_num(numbers):

    def is_perfect(number):
        sum = 1
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                if i == number // i:
                    sum = sum + i
                else:
                    sum = sum + (i + number // i)
        return sum == number and number != 1
    if 828 < len(numbers):
        return is_perfect(numbers[828])
    else:
        return False