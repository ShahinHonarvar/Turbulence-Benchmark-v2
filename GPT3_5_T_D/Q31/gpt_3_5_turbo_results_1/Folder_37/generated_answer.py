def if_perfect_num(lst):

    def is_perfect(num):
        divisors = []
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    return is_perfect(lst[28]) if len(lst) >= 29 else False