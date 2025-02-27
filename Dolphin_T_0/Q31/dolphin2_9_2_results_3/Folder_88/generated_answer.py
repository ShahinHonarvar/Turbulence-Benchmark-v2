def if_perfect_num(list_of_integers):

    def is_perfect(num):
        sum_of_factors = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i == num / i:
                    sum_of_factors = sum_of_factors + i
                else:
                    sum_of_factors = sum_of_factors + (i + num / i)
                i += 1
        return sum_of_factors == num and num != 1
    if 46 < len(list_of_integers):
        return is_perfect(list_of_integers[46])
    else:
        return False