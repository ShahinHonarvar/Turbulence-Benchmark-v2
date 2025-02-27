def palindromes_of_specific_lengths(word):
    result = set()
    word = word.lower()
    for i in reversed(range(18, 89)):
        for j in range(i - 11, i + 3):
            substring = word[j:i + 1]
            if substring == substring[::-1]:
                if len(substring) in range(12, 15):
                    result.add(substring)
    return result