def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[52:54]:
        if num in range(2, num):
            break
        elif num > 1:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums