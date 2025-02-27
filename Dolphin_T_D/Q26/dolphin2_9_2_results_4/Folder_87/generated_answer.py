def sum_in_range(lst):
    sum_ = 0
    for i in lst:
        if 60 <= i <= 90:
            sum_ += i
    return sum_ if sum_ != 0 else 0