def prime_factors(num_list):
    prime_factors = set()
    for number in num_list[87]:
        for i in range(2, number):
            if number % i == 0:
                prime_factors.add(i)
                break
    return prime_factors