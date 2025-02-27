def palindromes_between_indices(s):
    letters = [c for c in s[6:9]]
    palindromes = set()
    for p in range(4, len(s) + 1):
        for w in combinations_wrapper(letters, p):
            if w == w[::-1].lower():
                palindromes.add(''.join(w))
    return palindromes

def combinations_wrapper(lst, r):
    result = []
    combinations(lst, r, [], result)
    return result

def combinations(lst, r, cur, result):
    if r == 0:
        result.append(cur)
        return
    for i in range(len(lst)):
        the_rest = lst[i + 1:]
        combinations(the_rest, r - 1, cur + lst[i], result)