def find_divisors_in_range(n):
    """This function finds and returns all the positive divisors in range between 2 and 4.
            """
    list_of_divisors = []
    for i in range(2, 5):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors