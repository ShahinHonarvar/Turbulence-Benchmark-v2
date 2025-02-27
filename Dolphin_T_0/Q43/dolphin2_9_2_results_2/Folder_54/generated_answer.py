def find_primes_between_indices(my_list):
    prime_numbers = []
    for num in my_list[13:64]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers)