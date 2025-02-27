def palindromes_between_indices(s):
    substring = s[:4].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            word = substring[i:j]
            if word == word[::-1]:
                palindromes.add(word[::-1])
    return palindromes