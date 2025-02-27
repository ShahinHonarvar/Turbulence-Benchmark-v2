def palindromes_of_specific_lengths(text):
    subtext = text[17:73]
    palindromes = set()
    for i in range(len(subtext) - 50):
        substring = subtext[i:i + 51].lower()
        if substring == substring[::-1] and substring.isalpha() and (len(substring) in range(50, 52)):
            palindromes.add(substring)
    return palindromes