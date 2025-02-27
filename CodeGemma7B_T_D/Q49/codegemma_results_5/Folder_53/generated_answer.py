def if_decimal_is_divisible(bstr):

    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    def generate_fib_dividees(limit):
        fib_list = []
        for n in range(limit):
            fib_list.append(fib(n) // 64)
        return fib_list
    flag = False
    fib_dividees = generate_fib_dividees(200)
    for number in fib_dividees:
        if int(bstr, 2) == number:
            flag = True
            break
    return flag