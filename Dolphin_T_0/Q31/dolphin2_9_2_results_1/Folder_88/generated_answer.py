def if_perfect_num(numbers):
    num = numbers[46]
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    if sum_ == num:
        return True
    else:
        return False