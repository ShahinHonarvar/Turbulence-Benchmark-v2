def if_perfect_num(numbers_list):
    if len(numbers_list) > 3:
        num = numbers_list[3]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False