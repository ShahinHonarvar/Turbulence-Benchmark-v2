def palindromes_of_length_n(n, text):
    palindromes = set()
    if len(text) < n:
        return palindromes
    for i in range(len(text) - n + 1):
        candidate = text[i:i + n].lower()
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes