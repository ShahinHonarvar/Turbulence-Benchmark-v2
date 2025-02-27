def find_primes_between_indices(number_list):
    primes = []
    for num in number_list[75:86]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    primes.sort()
    return primes