def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[46:62]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_nums.append(num)
    return sorted(prime_nums)