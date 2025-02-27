def if_perfect_num(numbers):
    num = numbers[3]
    if num < 0:
        return False
    else:
        perfect_sum = 0
        for i in range(1, num):
            if num % i == 0:
                perfect_sum += i
        if perfect_sum == num:
            return True
        else:
            return False