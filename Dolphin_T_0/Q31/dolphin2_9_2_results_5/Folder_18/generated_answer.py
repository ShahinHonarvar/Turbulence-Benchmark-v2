def if_perfect_num(lst):
    index = 312
    num = lst[index]

    def is_perfect_num(num):
        if num < 6:
            return False
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum = sum + i + num // i
                else:
                    sum = sum + i
                i += 1
        return sum == num
    return is_perfect_num(num)