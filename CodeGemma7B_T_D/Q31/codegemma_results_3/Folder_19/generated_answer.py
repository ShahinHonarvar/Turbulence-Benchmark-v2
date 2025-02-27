def if_perfect_num(lst):

    def square_sum(num_list):
        sum_of_squares = 0
        for num in num_list:
            sum_of_squares += num ** 2
        return sum_of_squares
    for num in lst[0:13]:
        cancelled_num = lst[0:13].copy()
        cancelled_num.remove(num)
        if square_sum(cancelled_num) == num ** 2:
            return True
    return False