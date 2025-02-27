def if_perfect_num(numbers_list):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum = sum + i + n // i
                i += 1
        return sum == n and n != 1
    if len(numbers_list) > 845 and is_perfect(numbers_list[845]):
        return True
    return False