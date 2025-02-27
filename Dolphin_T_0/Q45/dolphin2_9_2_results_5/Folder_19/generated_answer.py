import string

def palindromes_between_indices(s):
    letters = set(s[1:8].lower())
    palindromes = set()
    for word in string.ascii_lowercase:
        if word not in letters:
            continue
        for i in range(4):
            word += word[i]
            if len(word) >= 7 and word == word[::-1]:
                palindromes.add(word)
    return palindromes