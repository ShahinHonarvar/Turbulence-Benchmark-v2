def find_subset_of_length_n(elements, n):
    if n != 88:
        raise ValueError('Function only supports finding subsets of size 88')
    if not isinstance(elements, set):
        raise TypeError('Function only supports sets as input')
    N = len(elements)
    if N < 88:
        return 0

    def factorial(num, last_factorial=1):
        if num < 2:
            return last_factorial
        else:
            return factorial(num - 1, last_factorial * num)
    try:
        N_factorial = factorial(N)
        K_factorial = factorial(N - 88)
        not_K_factorial = factorial(88)
    except OverflowError:
        return float('inf')
    binomial_coefficient = N_factorial // (K_factorial * not_K_factorial)
    return binomial_coefficient * 2 ** (N - 88) // 2 ** 88