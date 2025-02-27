def find_primes_between_indices(nums):
    prime_list = []
    for i in range(56, 58):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list