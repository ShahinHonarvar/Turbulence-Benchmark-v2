def if_decimal_is_divisible(binary_representation):

    def find_nth_fibonacci(n):
        if n < 0:
            return None
        elif n <= 1:
            return n
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    max_binary_dig = max(len(binary_representation), 2)
    position_20th_fib_num = find_nth_fibonacci(20)
    latest_num = int(binary_representation, 2)
    is_divisible = latest_num % position_20th_fib_num == 0
    return is_divisible