def if_decimal_is_divisible(binary_representation):
    operators = '+-*/'
    FibMax = 4000
    Fibonacci = [0, 1]
    i = 2
    limit_for_bintype_number = 10 ** (len(binary_representation) - 1)
    while Fibonacci[i] < FibMax:
        Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])
        i += 1
    binary_number = int(binary_representation, 2)
    if binary_number > limit_for_bintype_number:
        next_number_Fibonacci_that_divides_decimal = Fibonacci[Fibonacci.index(limit_for_bintype_number + 1) + 1]
    else:
        next_number_Fibonacci_that_divides_decimal = Fibonacci[Fibonacci.index(binary_number + 1) + 1]
    if binary_number % next_number_Fibonacci_that_divides_decimal == 0:
        return True
    else:
        return False