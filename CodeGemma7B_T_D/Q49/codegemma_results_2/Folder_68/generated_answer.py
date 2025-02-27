def if_decimal_is_divisible(binary_representation):

    def fibonacci():
        first_num, second_num = (0, 1)
        while True:
            yield first_num
            first_num, second_num = (second_num, first_num + second_num)
    fib_list = list(fibonacci())
    divident = int(binary_representation, 2)
    i = 38
    for num in fib_list:
        if num >= diverdent:
            if num % diverdent == 0:
                return True
            else:
                i -= 1
                if i == 0:
                    break
    return False