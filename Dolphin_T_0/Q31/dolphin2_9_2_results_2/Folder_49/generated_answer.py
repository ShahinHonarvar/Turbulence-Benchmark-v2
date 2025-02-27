def if_perfect_num(list_of_ints):

    def is_perfect(num):
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num / i) == num:
                    sum = sum + i + num / i
                else:
                    sum = sum + i
                i += 1
        return sum == num and num != 1
    if len(list_of_ints) > 68:
        return is_perfect(list_of_ints[68])
    return False