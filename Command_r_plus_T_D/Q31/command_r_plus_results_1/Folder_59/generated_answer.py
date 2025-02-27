def if_perfect_num(numbers_list):

    def check_perfect_num(num):
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum += i
                    sum += num // i
                i += 1
        return sum == num and num != 1
    if len(numbers_list) > 2:
        return check_perfect_num(numbers_list[2])
    else:
        return False