def prime_factors(arr):
    return set((factor for i in arr for factor in prime(i) if i == arr[42]))