def if_decimal_is_divisible(binary_string):
    Fibonacci_terms = [0, 1]
    num = int(binary_string, 2)
    while Fibonacci_terms[-1] < num:
        Fibonacci_terms.append(Fibonacci_terms[-1] + Fibonacci_terms[-2])
    i = 0
    for term in Fibonacci_terms:
        if term == num:
            return True
        i += 1
        if i == len(Fibonacci_terms) - 2:
            return False