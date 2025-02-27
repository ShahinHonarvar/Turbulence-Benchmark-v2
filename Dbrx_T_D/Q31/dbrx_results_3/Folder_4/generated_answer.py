def if_perfect_num(int_list):
    if len(int_list) > 15:
        return int_list[15].is_perfect()
    else:
        return False

def is_perfect(n):
    return n == sum((i for i in range(1, n) if n % i == 0))