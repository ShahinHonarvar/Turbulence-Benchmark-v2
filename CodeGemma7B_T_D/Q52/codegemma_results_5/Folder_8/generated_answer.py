def palindrome_of_length_n(text):
    palindromes = [text[i:i + 49] for i in range(len(text) - 49 + 1)]
    palindromes = [p for p in palindromes if p.lower() == p[::-1].lower()]
    return set(palindromes)