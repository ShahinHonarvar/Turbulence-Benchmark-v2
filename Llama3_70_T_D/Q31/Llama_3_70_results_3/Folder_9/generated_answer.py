def if_perfect_num(num_list):

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    if len(num_list) <= 24:
        return False
    else:
        return is_perfect(num_list[24])