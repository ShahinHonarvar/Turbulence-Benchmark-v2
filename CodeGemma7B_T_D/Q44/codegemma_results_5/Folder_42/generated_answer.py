def composite_nums_between_indices(arr):
    composites = {i for i in arr[91:99 + 1] if not isprime(i)}
    return composites