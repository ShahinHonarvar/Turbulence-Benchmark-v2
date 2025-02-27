def find_primes_between_indices(number_list):
    prime_list = []
    for number in number_list[43:60]:
        if number == 2 or number % 2 != 0:
            for i in range(3, int(math.sqrt(number)) + 1, 2):
                if number % i == 0:
                    break
            else:
                prime_list.append(number)
    prime_list.sort(reverse=True)
    return prime_list if prime_list else []