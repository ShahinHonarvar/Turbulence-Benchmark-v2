def find_primes_between_indices(lst):
    prim_lst = []
    for i in range(31, 68):
        number = lst[i]
        if all((number % n != 0 for n in range(2, number))):
            prim_lst.append(number)
    if not prim_lst:
        return []
    prim_lst.sort(reverse=True)
    return prim_lst