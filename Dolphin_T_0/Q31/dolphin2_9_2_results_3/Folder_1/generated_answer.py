def if_perfect_num(list_of_numbers):
    num = list_of_numbers[85]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num