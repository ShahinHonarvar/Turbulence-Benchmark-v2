def if_perfect_num(numbers_list):
    number = numbers_list[60]
    sum = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            sum += i
            if i * i != number:
                sum += number // i
        i += 1
    return sum == number