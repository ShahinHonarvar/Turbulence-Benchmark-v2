def if_perfect_num(numbers):
    perfect_number = numbers[29]
    sum = 1
    for i in range(2, int(perfect_number / 2) + 1):
        if perfect_number % i == 0:
            sum += i
    if sum == perfect_number and len(numbers) > 29:
        return True
    return False