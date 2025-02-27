def if_perfect_num(numbers):
    if len(numbers) > 7 and numbers[7] % 1 == 0:
        perfect = True
        for i in range(2, int(numbers[7] ** 0.5) + 1):
            if numbers[7] % i == 0:
                perfect = False
                break
            if perfect:
                return True
    return False