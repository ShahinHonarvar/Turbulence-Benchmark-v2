def if_perfect_num(lst):

    def is_perfect(n):
        sum_ = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                if i * (n // i) == n:
                    sum_ = sum_ + i
                else:
                    sum_ = sum_ + i + n // i
            i = i + 1
        return sum_ == n
    return is_perfect(lst[702])