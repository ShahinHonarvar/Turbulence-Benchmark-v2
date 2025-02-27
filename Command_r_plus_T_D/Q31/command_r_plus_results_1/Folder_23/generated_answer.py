def if_perfect_num(numbers_list):

    def check_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif n / i != i:
                sum = sum + i
                n = n / i
            else:
                sum = sum + i
                break
        return sum + n == n
    if len(numbers_list) > 69 and check_perfect(numbers_list[69]):
        return True
    else:
        return False