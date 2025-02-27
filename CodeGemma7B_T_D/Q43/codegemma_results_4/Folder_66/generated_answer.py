def find_primes_between_indices(lst):
    prime_list = []
    for number in lst[72:73]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime_list.append(number)
    return sorted(prime_list)