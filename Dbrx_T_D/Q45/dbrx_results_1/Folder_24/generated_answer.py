from sets import Set

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = Set()
    for i in range(2, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) >= 4 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes