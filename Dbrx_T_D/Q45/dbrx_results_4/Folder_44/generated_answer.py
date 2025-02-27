import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    substr = s[2:8].lower()
    palindromes = set()
    for i in range(len(substr) - 2):
        for j in range(i, len(substr) - i):
            candidate = substr[i:j + 1] + substr[i:j][::-1]
            if candidate[0] in english_letters and candidate == candidate.lower():
                palindromes.add(candidate)
    return palindromes