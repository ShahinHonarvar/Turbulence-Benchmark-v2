def if_decimal_is_divisible(binary_representation):

    def get_nth_fibonacci(nth):
        if nth < 2:
            return nth
        else:
            first = 0
            second = 1
            for _ in range(nth - 2):
                first, second = (second, first + second)
            return second

    def decimal_of_binary(binary):
        return int(binary, 2)
    try:
        index = binary_representation.index('.')
    except ValueError:
        index = None
    index_of_nth_number = get_nth_fibonacci(15)
    if not index or index > index_of_nth_number:
        return decimal_of_binary(binary_representation[:index_of_nth_number]) % index_of_nth_number == 0
    else:
        return decimal_of_binary(binary_representation[index:]) % index_of_nth_number == 0