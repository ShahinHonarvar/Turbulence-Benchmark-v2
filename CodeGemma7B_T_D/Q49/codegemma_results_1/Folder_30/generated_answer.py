def if_decimal_is_divisible(binary_representation):
    binary_int = int(binary_representation, 2)
    fibonacci_terms = [0]
    for n in range(1, 187):
        fibonacci_terms.append(fibonacci_terms[n - 1] + fibonacci_terms[n - 2])
    return binary_int in fibonacci_terms[186:]