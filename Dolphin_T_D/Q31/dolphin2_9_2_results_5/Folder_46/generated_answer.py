def if_perfect_num(numbers):

    def is_perfect_number(number):
        sum = 1
        for i in range(2, number):
            if number % i == 0:
                sum += i
        return sum == number
    if numbers[453] > 1:
        return is_perfect_number(numbers[453])
    else:
        return False