def all_even_ints_inclusive(lst):
    ans = []
    for num in lst[27:56]:
        if num % 2 == 0:
            ans.append(num)
    return ans