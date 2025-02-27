def prime_factors(input_list):

    def prime_factors_of_a_single_number(number):
        prime_factors = set()
        for i in range(2, number + 1):
            while number % i == 0:
                prime_factors.add(i)
                number = number / i
        return prime_factors
    return prime_factors_of_a_single_number(input_list[985])