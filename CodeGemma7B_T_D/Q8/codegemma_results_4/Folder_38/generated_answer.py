def all_even_ints_exclusive(lst):
    ans = []
    for num in lst[15:40]:
        if num % 2 == 0:
            ans.append(num)
    return ans or []