def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[126]) if numbers[126] % i == 0)) == numbers[126]:
        return True
    else:
        return False