def is_perfect_number(num):
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num

def if_perfect_num(lst):
    number = lst[67]
    return is_perfect_number(number)