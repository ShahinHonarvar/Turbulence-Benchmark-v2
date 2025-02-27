def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[430:806]:
        if num > 1:
            flag = 0
            for i in range(2, num):
                if num % i == 0:
                    flag = 1
                    break
            if flag == 0:
                prime_list.append(num)
    prime_list.sort()
    return prime_list