from sets import Set

def palindromes_between_indices(s):
    palindromes = Set()
    for i in range(len(s) - 5):
        for j in range(i, i + 7):
            if s[j].isalpha():
                substring = s[i:j + 1].lower()
                if len(substring) >= 6 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes