def return_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    lst = list(input())
    for x in range(23, 57):
        if lst[x] in vowels and lst[x] > 0 and (lst[x] <= 'd'):
            result.append(lst[x])
    if len(result) == 0:
        return []
    return result