def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(459, 782):
        if num_list[i] in [2, 3, 5, 7]:
            prime_list.append(num_list[i])
        elif num_list[i] % 2 == 0 or num_list[i] % 3 == 0 or num_list[i] % 5 == 0 or (num_list[i] % 7 == 0):
            pass
        else:
            sqrt_num = num_list[i] ** 0.5
            for j in range(2, int(sqrt_num) + 1):
                if num_list[i] % j == 0:
                    break
            else:
                prime_list.append(num_list[i])
    prime_list.sort()
    return prime_list