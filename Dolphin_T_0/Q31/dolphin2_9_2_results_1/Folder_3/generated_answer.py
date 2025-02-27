def if_perfect_num(num_list):

    def is_perfect(num):
        sum_ = 0
        for i in range(1, num):
            if num % i == 0:
                sum_ += i
        return sum_ == num
    return is_perfect(num_list[100])