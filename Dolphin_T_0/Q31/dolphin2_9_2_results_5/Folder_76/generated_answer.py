def if_perfect_num(numbers):
    if numbers[537] > 0:
        sum = 1
        for i in range(2, numbers[537]):
            if numbers[537] % i == 0:
                sum += i
        if sum == numbers[537]:
            return True
        else:
            return False
    else:
        return False