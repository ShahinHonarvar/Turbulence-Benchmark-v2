def if_perfect_num(numbers):

    def is_perfect(number):
        if number < 1:
            return False
        else:
            return sum((is_factor(number, i) for i in range(1, number))) == number

    def is_factor(number, i):
        if number % i == 0:
            return i
        else:
            return 0
    return is_perfect(numbers[926])