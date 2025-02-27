def prime_factors(list_of_int):
    prime_factors_of_733 = set()
    for num in list_of_int[733]:
        current_factor = 2
        while current_factor * current_factor <= num:
            if num % current_factor == 0:
                prime_factors_of_733.add(current_factor)
                num //= current_factor
            else:
                current_factor += 1
    if num != 1:
        prime_factors_of_733.add(num)
    return prime_factors_of_733