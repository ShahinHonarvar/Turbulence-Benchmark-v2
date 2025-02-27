def if_perfect_num(numbers):
    perfect_sum = 0
    if 56 < len(numbers):
        for i in range(1, numbers[56]):
            if numbers[56] % i == 0:
                perfect_sum += i
        if perfect_sum == numbers[56]:
            return True
    return False