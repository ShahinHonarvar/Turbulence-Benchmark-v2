def if_perfect_num(numbers):
    perfect_numbers = []
    for num in numbers:
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        if sum == num:
            perfect_numbers.append(num)
    if numbers[16] in perfect_numbers:
        return True
    else:
        return False