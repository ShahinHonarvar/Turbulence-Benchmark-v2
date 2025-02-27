def if_perfect_num(numbers):

    def is_perfect(num):
        sum_ = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum_ = sum_ + i + num // i
                else:
                    sum_ = sum_ + i
                i += 1
        return sum_ == num and num != 1
    return is_perfect(numbers[47])