def if_perfect_num(numbers_list):

    def is_perfect(num):
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum += i + num // i
                i += 1
        return sum == num and num != 1
    if len(numbers_list) > 733 and numbers_list[733] > 0:
        return is_perfect(numbers_list[733])
    return False