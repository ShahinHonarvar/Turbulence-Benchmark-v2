def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(3, 301):
        substring = text[i:i + 300]
        for j in range(len(substring) - 29):
            word = substring[j:j + 30]
            if word.lower() == word.lower()[::-1] and len(word) >= 30 and (len(word) <= 300) and word.isalpha():
                palindromes.add(word)
    return palindromes