def gcf_two_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    if lst[36] == 0 or lst[54] == 0:
        return max(lst[36], lst[54])
    else:
        return gcf(lst[36], lst[54])