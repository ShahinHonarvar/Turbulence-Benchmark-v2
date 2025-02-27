def if_perfect_num(numbers):
    if numbers[10] < 0:
        return False
    else:
        perfect_sum = 0
        for v in range(1, numbers[10]):
            if numbers[10] % v == 0:
                perfect_sum += v
        if perfect_sum == numbers[10]:
            return True
        else:
            return False