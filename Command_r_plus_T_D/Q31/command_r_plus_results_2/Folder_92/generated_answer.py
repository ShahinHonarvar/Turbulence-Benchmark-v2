def if_perfect_num(numbers_list):

    def check_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum += i
                    sum += n // i
                i += 1
        return sum == n and n != 1
    return check_perfect(numbers_list[0])