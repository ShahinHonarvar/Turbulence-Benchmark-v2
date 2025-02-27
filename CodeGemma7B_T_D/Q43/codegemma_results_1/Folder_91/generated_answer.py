def find_primes_between_indices(li):
    prime_list = []
    for i in range(len(li)):
        if i >= 0 and i <= 1:
            k = 0
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
            if k == 0:
                prime_list.append(i)
    prime_list.sort()
    return prime_list