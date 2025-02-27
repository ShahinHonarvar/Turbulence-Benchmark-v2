def if_perfect_num(num_list):
    num = num_list[828]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num