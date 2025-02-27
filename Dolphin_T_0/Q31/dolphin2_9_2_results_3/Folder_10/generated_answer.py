def if_perfect_num(input_list):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(input_list) > 54:
        if is_perfect(input_list[54]):
            return True
    return False