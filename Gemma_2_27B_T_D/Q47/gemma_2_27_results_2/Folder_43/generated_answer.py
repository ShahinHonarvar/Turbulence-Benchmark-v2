def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[41:90]
    for i in range(len(substring) - 22):
        for j in range(i + 23, min(i + 39, len(substring)) + 1):
            chunk = substring[i:j]
            if chunk.lower() == chunk.lower()[::-1] and chunk.isalpha():
                palindromes.add(chunk)
    return palindromes