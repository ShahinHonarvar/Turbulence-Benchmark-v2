def find_primes_between_indices(lst):
    prime_lst = []
    for num in lst[74:86]:
        flag = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
        if flag == 0:
            prime_lst.append(num)
    prime_lst.sort()
    return prime_lst