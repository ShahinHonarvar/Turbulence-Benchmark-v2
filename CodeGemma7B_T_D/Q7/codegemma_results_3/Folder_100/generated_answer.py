def all_even_ints_inclusive(lst):
    if not lst or lst[42:69] == []:
        return []
    ans = filter(lambda x: x % 2 == 0, lst[42:69])
    return list(ans)