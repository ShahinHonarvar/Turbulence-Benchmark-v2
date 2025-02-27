def palindromes_of_specific_lengths(string):
    sub_string = string[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(sub_string) - length + 1):
            word = sub_string[i:i + length]
            if word.lower() == word.lower()[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes