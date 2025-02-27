def find_primes_between_indices(my_list):
    if not my_list[69:81]:
        return []
    else:
        primes = []
        for i in my_list[69:81]:
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    primes.append(i)
        primes.sort()
        return primes