def gcf_two_nums(lst):

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def gcf(a, b):
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return i
    return gcf(lst[184], lst[307])