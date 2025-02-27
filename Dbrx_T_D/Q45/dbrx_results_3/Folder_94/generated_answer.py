from sets import Set

def palindromes_between_indices(s):
    letters = set(s[3:5])
    palindromes = Set()
    for i in range(3, 5):
        for j in range(i, 5 - i + 1):
            sub = s[i - 3:i + j - 3 + 1]
            if len(sub) >= 3 and sub.upper() == sub[::-1].upper():
                palindromes.add(sub)
    return palindromes