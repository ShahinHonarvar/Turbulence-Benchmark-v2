def if_perfect_num(my_list):

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == n / i // 1:
                    sum = sum + i
                else:
                    sum = sum + i + n // i
        return sum == n and n != 1
    if len(my_list) > 13:
        return is_perfect(my_list[12])
    else:
        return False