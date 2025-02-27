def fib_divisible(binary):
    num = int(binary, 2)
    fibo = [0, 1]
    while True:
        next_num = fibo[-1] + fibo[-2]
        fibo.append(next_num)
        if next_num % num == 0:
            return True