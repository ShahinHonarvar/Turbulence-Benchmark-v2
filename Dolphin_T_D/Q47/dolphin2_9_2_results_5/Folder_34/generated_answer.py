def palindromes_of_specific_lengths(string):
    substring = string[200:301]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word.lower() == word.lower()[::-1]:
                for letter in word:
                    if not letter.isalpha():
                        break
                else:
                    palindromes.add(word)
    return palindromes