def prime_factors(number_list):
    prime_factors_set = set()
    for number in number_list:
        for divisor in range(2, number):
            if number % divisor == 0:
                prime_factors_set.add(divisor)
    for divisor in range(2, number_list[410]):
        if number_list[410] % divisor == 0:
            prime_factors_set.add(divisor)
    return prime_factors_set