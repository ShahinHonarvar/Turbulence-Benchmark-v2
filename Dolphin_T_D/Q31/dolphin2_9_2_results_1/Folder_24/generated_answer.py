def if_perfect_num(lst):

    def is_perfect(n):
        if n < 0:
            return False
        else:
            result = 0
            for i in range(1, n):
                if n % i == 0:
                    result += i
            return result == n
    return is_perfect(lst[74])