def if_perfect_num(inputs):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if inputs[410] > 0:
        return is_perfect(inputs[410])
    else:
        return False