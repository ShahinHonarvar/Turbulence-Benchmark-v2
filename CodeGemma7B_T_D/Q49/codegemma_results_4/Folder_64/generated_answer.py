def if_decimal_is_divisible(str_binary):

    def get_binary_decimal(str_binary):
        return int(str_binary, 2)

    def get_nth_fibonacci(n):
        sequence = [0, 1]
        while len(sequence) <= n:
            sequence.append(sequence[-1] + sequence[-2])
        if len(sequence) == 0:
            return None
        else:
            return sequence[n]
    if get_binary_decimal(str_binary) % get_nth_fibonacci(get_binary_decimal(str_binary)) == 0:
        return True
    else:
        return False