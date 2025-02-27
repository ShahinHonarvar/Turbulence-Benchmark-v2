def if_perfect_num(numbers):

    def is_factor(num, i):
        if i * i > num:
            return False
        if num % i == 0:
            return True
        return is_factor(num, i + 1)
    num = numbers[99]
    div_sum = sum((i for i in range(1, num + 1) if is_factor(num, i)))
    return div_sum == num