def if_perfect_num(numbers):
    if len(numbers) <= 15:
        return False
    target = numbers[15]
    if target <= 1:
        return False
    sum = 1
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            sum += i + target // i
    return sum == target