def find_primes_between_indices(arr):
    primes_list = []
    for num in arr[261:460]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes_list.append(num)
    return sorted(primes_list)