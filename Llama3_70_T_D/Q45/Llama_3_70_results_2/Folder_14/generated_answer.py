def palindromes_between_indices(s):
    s = s[4:6].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in get_palindromes(s, i):
            palindromes.add(p)
    return palindromes

def get_palindromes(s, n):
    if n == 1:
        return [c for c in s]
    elif n == 2:
        return [c + c for c in s]
    else:
        palindromes = set()
        for c in s:
            for p in get_palindromes(s, n - 2):
                if p.count(c) < s.count(c):
                    palindromes.add(c + p + c)
        return palindromes