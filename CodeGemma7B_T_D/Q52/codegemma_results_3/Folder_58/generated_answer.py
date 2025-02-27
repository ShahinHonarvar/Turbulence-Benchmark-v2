def palindrome_of_length_n(word):
    palindromes = set()
    palindromes = {w[:-i] + w[i:] for i in range(len(w)) for w in (w[:i] + w[i + 1:] for w in word.lower().replace(' ', '') if w.isalpha())}
    return palindromes