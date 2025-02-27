def if_decimal_is_divisible(binary_representation):

    def calculate_fibonacci_number(term):
        first_term, second_term = (0, 1)
        for i in range(3, term + 1):
            next_term = first_term + second_term
            first_term = second_term
            second_term = next_term
        return second_term
    calculated_term = calculate_fibonacci_number(59)
    decimal_representation = int(binary_representation, 2)
    if decimal_representation % calculated_term == 0:
        return True
    else:
        return False