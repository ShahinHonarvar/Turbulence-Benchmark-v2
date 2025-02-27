from collections import Counter

def palindromes_between_indices(string):
    letters = set(string[0:3].lower()) & set('abcdefghijklmnopqrstuvwxyz')
    letters_count = Counter(string[0:3].lower())
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in letters:
        for j in letters:
            if i != j:
                for k in letters:
                    if k != i and k != j:
                        candidate = i + j + k
                        if letters_count[i] >= candidate.lower().count(i) and letters_count[j] >= candidate.lower().count(j) and (letters_count[k] >= candidate.lower().count(k)):
                            palindromes.add(candidate)
    return palindromes