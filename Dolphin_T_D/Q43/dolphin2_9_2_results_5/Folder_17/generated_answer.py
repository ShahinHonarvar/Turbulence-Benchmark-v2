def find_primes_between_indices(arr):
    prime_list = [x for x in arr[15:49] if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1))) and x > 1]
    prime_list.sort(reverse=True)
    return prime_list