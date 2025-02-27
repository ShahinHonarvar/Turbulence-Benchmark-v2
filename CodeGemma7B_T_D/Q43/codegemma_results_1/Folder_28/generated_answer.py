def find_primes_between_indices(numbers):
    prime_list = []
    for num in numbers[38:55]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list if prime_list else []