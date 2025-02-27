def if_decimal_is_divisible(bin_rep):
    fib_nums = get_fib_sequence_up_to(bin_rep.count('1') * 15)
    return int(bin_rep, 2) in fib_nums

def get_fib_sequence_up_to(n):
    fib_nums = [0, 1]
    while len(fib_nums) <= n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return fib_nums[:n + 1]