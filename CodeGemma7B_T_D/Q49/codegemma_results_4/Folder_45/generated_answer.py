def if_decimal_is_divisible(binary_str):
    fib_list = [0]
    fib_list.append(fib_list[-1] + fib_list[-2])
    while fib_list[-1] < 28:
        fib_list.append(fib_list[-1] + fib_list[-2])
    fib_list.pop()
    fib_num = int(binary_str, 2)
    if fib_num % fib_list[sbn_which_fibonacci(fib_list, 28)] == 0:
        return True
    else:
        return False

def sbn_which_fibonacci(fib_lst, num):
    if num in fib_lst:
        return fib_lst.index(num)
    else:
        return len(fib_lst)