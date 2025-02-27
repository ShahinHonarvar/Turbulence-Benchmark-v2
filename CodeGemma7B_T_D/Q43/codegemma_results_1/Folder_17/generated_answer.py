def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(15, 49):
        if int_list[i] > 1:
            for j in range(2, int_list[i]):
                if int_list[i] % j == 0:
                    break
            else:
                prime_list.append(int_list[i])
    prime_list.sort(reverse=True)
    return prime_list