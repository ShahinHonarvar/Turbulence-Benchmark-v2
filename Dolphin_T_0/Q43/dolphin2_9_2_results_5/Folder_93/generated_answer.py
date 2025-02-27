def find_primes_between_indices(input_list):
    prime_numbers = []
    for i in range(70, 72):
        num = input_list[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)