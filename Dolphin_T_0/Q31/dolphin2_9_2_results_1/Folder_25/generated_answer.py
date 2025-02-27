def if_perfect_num(numbers):

    def is_perfect(num):
        _sum = 0
        for i in range(1, num):
            if num % i == 0:
                _sum += i
        return num == _sum
    return is_perfect(numbers[90])