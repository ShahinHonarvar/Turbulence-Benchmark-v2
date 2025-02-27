def if_perfect_num(numbers):
    perfect_number = numbers[91]
    sum = 1
    for i in range(2, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            sum += i
            if i != perfect_number // i:
                sum += perfect_number // i
    return sum == perfect_number