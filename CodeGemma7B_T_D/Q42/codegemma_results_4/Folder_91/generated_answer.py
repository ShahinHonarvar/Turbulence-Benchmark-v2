def prime_factors(lst):
    six = lst[6]
    ans = set()
    for i in range(2, six + 1):
        while six % i == 0:
            ans.add(i)
            six //= i
    return ans