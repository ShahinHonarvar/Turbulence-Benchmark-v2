def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(20, 49):
        if int_list[i] in (2, 3, 5, 7):
            prime_list.append(int_list[i])
        elif int_list[i] % 2 == 0 or int_list[i] % 3 == 0 or int_list[i] % 5 == 0 or (int_list[i] % 7 == 0):
            pass
        else:
            for j in range(11, int_list[i], 2):
                if int_list[i] % j == 0:
                    break
            else:
                prime_list.append(int_list[i])
    prime_list.sort(reverse=True)
    return prime_list