def if_perfect_num(lst):

    def is_perfect(num):
        if num < 0:
            return False
        div_sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                div_sum += i
                if num // i != i:
                    div_sum += num // i
                i += 1
        return div_sum == num
    return is_perfect(lst[88])