def find_sum_of_multiples(arg):

    def inner_func(num):
        if num % arg == 0:
            return True
        return False
    ans = 0
    for i in range(1, 57):
        if inner_func(i):
            ans += i
    return ans