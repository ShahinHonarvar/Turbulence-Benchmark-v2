def if_perfect_num(numbers):
    sum = 1
    n = numbers[2]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i + n // i
    if sum == n and n != 1:
        return True
    else:
        return False