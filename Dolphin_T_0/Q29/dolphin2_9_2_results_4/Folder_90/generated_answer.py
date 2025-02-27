def gcf_two_nums(num_list):
    a = num_list[634]
    b = num_list[585]

    def gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    return gcf(a, b)