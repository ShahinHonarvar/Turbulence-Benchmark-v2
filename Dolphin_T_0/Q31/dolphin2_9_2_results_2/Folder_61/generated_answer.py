def if_perfect_num(lst):

    def is_perfect(n):
        sum_ = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == n // i:
                    sum_ += i
                else:
                    sum_ += i + n // i
        return sum_ == n and n != 1
    return is_perfect(lst[8])