from sets import Set

def palindromes_between_indices(s):
    palindromes = Set()
    for i in range(len(s) - 2):
        for j in range(i + 1, min(i + 4, len(s))):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes